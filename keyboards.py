from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(
    resize_keyboard=True
)
start.row(
    KeyboardButton(text='🤖 ПЕРЕЙТИ В БОТА 🤖')
)
start.row(
    KeyboardButton(text='🙏 НУЖНА ПОМОЩЬ 🙏')
)

go_to_bot = InlineKeyboardMarkup()
go_to_bot.row(InlineKeyboardButton('🤖 Перейти в бота 🤖', url='https://t.me/DanyaLucky3_bot'))

big_money = InlineKeyboardMarkup()
big_money.row(
    InlineKeyboardButton('💵 Начать зарабатывать 💵', url='https://t.me/DanyaLucky3_bot')
)