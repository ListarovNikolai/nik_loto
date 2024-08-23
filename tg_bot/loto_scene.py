from aiogram.fsm.scene import Scene, SceneRegistry, ScenesManager, on
from typing import Any

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.scene import Scene, SceneRegistry, ScenesManager, on
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram.types import KeyboardButton, Message, ReplyKeyboardRemove
from aiogram.utils.formatting import (
    Bold,
    as_key_value,
    as_list,
    as_numbered_list,
    as_section,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from nik_loto.keg import Keg
from nik_loto.player import ComputerPlayer, HumanPlayer, TgPlayer


class LotoScene(Scene, state="loto"):
    """
    This class represents a scene for a loto game.

    It inherits from Scene class and is associated with the state "loto".
    It handles the logic and flow of the loto game.
    """

    @on.message.enter()
    async def on_enter(self, message: Message, state: FSMContext, step: int | None = 0) -> Any:
        #await message.answer(f"Добро пожаловать в игру лото1 {message.from_user.first_name}!")
        if not step:
            # This is the first step, so we should greet the user
            step = 0
            await message.answer(f"Добро пожаловать в игру лото {message.from_user.first_name}!")

        try:
            my_keg = Keg()
            c_player = ComputerPlayer()
            tg_player = TgPlayer(message.from_user.first_name)
            # await message.answer(f"Новый мешок: \n{my_keg}")
        except Exception as e:
            await message.answer(f"Возникла ошибка: \n{e}")
            return await self.wizard.exit()

        next_number = my_keg.get_keg()
        await message.answer(f"Выпал бочонок под номером {html.bold(next_number)}!")
        markup = ReplyKeyboardBuilder()
        #markup.add(*[KeyboardButton(text=answer.text) for answer in quiz.answers])
        markup.button(text="✅ Да")
        markup.button(text="❌ Нет")

        if step > 0:
            markup.button(text="🔙 Back")
        markup.button(text="🚫 Exit")

        await state.update_data(step=step,
                                my_keg=my_keg,
                                c_player=c_player,
                                tg_player=tg_player,
                                next_number=next_number)

        await message.answer(tg_player.card.__str__())
        return await message.answer(
            text="Зачеркнуть?",
            reply_markup=markup.adjust(2).as_markup(resize_keyboard=True),
        )

    @on.message.exit()
    async def on_exit(self, message: Message, state: FSMContext) -> None:
        """
        Method triggered when the user exits the quiz scene.

        It calculates the user's answers, displays the summary, and clears the stored answers.

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        answers = data.get("answers", {})

        correct = 0
        incorrect = 0
        user_answers = []

        await message.answer("Игра закончена", reply_markup=ReplyKeyboardRemove())
        await state.set_data({})

    @on.message(F.text=="✅ Да")
    async def yes_handler(self, message: Message, state: FSMContext) -> None:
        """
        Это обработчик клавиши да

        :param message:
        :param state:
        :return:
        """
        data = await state.get_data()
        decision="y"
        next_number = data.get("next_number")
        tg_player = data.get("tg_player")
        tg_player.move(next_number, decision)

@on.message(F.text=="❌ Нет")
    async def no_handler(self, message: Message, state: FSMContext) -> None:
        """
        Это обработчик хода

        :param message:
        :param state:
        :return:
        """
        pass




loto_router = Router(name=__name__)
loto_router.message.register(LotoScene.as_handler(), Command("loto"))