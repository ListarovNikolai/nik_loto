from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_answer = ReplyKeyboardBuilder()
#markup.add(*[KeyboardButton(text=answer.text) for answer in quiz.answers])
kb_answer.button(text="✅ Да")
kb_answer.button(text="❌ Нет")
kb_answer.button(text="🚫 Exit")
