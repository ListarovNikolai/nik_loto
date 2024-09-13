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

from nik_loto.game import game_over, find_winners
from nik_loto.keg import Keg
from nik_loto.player import ComputerPlayer, HumanPlayer, TgPlayer
from tg_bot.keyboard import kb_answer


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
            players = [c_player, tg_player]
            # await message.answer(f"Новый мешок: \n{my_keg}")
        except Exception as e:
            await message.answer(f"Возникла ошибка: \n{e}")
            return await self.wizard.exit()

        next_number = my_keg.get_keg()
        await message.answer(f"Выпал бочонок под номером {html.bold(next_number)}!")
        await state.update_data(step=step,
                                my_keg=my_keg,
                                next_number=next_number,
                                players=players)

        await message.answer(tg_player.card.__str__())
        return await message.answer(
            text="Зачеркнуть?",
            reply_markup=kb_answer.adjust(2).as_markup(resize_keyboard=True),
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
        players = data.get("players")
        my_keg = data.get("my_keg")
        step = data.get("step")
        c_player = players[0]
        tg_player = players[1]
        winners = find_winners(players)
        if len(winners) == 0:
            await message.answer(f"{message.from_user.first_name}, Вы проиграли!", reply_markup=ReplyKeyboardRemove())
        else:
            for winner in winners:
                await message.answer(f"{winner.name}, - ПОБЕДИТЕЛЬ!",
                                     reply_markup=ReplyKeyboardRemove())
        await message.answer("Игра закончена", reply_markup=ReplyKeyboardRemove())
        await state.set_data({})

    @on.message(F.text == "✅ Да")
    async def yes_handler(self, message: Message, state: FSMContext) -> Any:
        """
        Это обработчик клавиши да

        :param message:
        :param state:
        :return:
        """
        decision = "y"
        data = await state.get_data()
        next_number = data.get("next_number")
        players = data.get("players")
        my_keg = data.get("my_keg")
        step = data.get("step")
        c_player = players[0]
        tg_player = players[1]

        tg_player.move(next_number, decision)
        c_player.move(next_number)
        players = [c_player, tg_player]

        if game_over(players):
            return await self.wizard.exit()

        next_number = my_keg.get_keg()
        step += 1
        await message.answer(f"Выпал бочонок под номером {html.bold(next_number)}!")
        await state.update_data(step=step,
                                my_keg=my_keg,
                                next_number=next_number,
                                players=players)

        await message.answer(tg_player.card.__str__())
        return await message.answer(
            text="Зачеркнуть?",
            reply_markup=kb_answer.adjust(2).as_markup(resize_keyboard=True),
        )

    @on.message(F.text == "❌ Нет")
    async def no_handler(self, message: Message, state: FSMContext) -> Any:
        """
        Это обработчик хода

        :param message:
        :param state:
        :return:
        """
        decision = "n"
        data = await state.get_data()
        next_number = data.get("next_number")
        players = data.get("players")
        my_keg = data.get("my_keg")
        step = data.get("step")
        c_player = players[0]
        tg_player = players[1]

        tg_player.move(next_number, decision)
        c_player.move(next_number)
        players = [c_player, tg_player]

        if game_over(players):
            return await self.wizard.exit()

        next_number = my_keg.get_keg()
        step += 1
        await message.answer(f"Выпал бочонок под номером {html.bold(next_number)}!")
        await state.update_data(step=step,
                                my_keg=my_keg,
                                next_number=next_number,
                                players=players)

        await message.answer(tg_player.card.__str__())
        return await message.answer(
            text="Зачеркнуть?",
            reply_markup=kb_answer.adjust(2).as_markup(resize_keyboard=True),
        )


loto_router = Router(name=__name__)
loto_router.message.register(LotoScene.as_handler(), Command("loto"))
