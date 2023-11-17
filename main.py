import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import keyboards
import db_api
from aiogram.types import Message, ChatJoinRequest, MediaGroup
import sender

TOKEN = '6447292179:AAGCgLqv-cgLHr5lIYnB_6R7kQsZuAn9S6o'
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
sender.set_bot(dp)
sender.init_handlers()


@dp.message_handler(commands=['start'])
async def start(message: Message):
    db_api.add_user(message.chat.id)
    path = os.path.join(os.path.dirname(__file__), 'img', 'start.png')
    f = open(path, 'rb')

    await message.answer_photo(
        photo=f,
        caption='Бро, спасибо, что проявил <b>инициативу</b>!\n'
        'Я ценю это в людях, а ещё это значит, что ты правда хочешь заработать 💸\n\n'
        'Для того чтобы начать тебя всего лишь надо выполнить все шаги в моём боте 👉🏻 @Lucky_hackjet_bot 👈🏻\n'
        'После их выполнения ты получишь бесплатный доступ в мой частный канал с сигналами на целых 3 дня ⌛️',
        parse_mode='html',
        reply_markup=keyboards.start
    )

    f.close()


@dp.message_handler(lambda m: m.text == '🤖 ПЕРЕЙТИ В БОТА 🤖')
async def get_bot(message: Message):
    await message.answer(
        '⚡️Скорее переходи в бота и проходи все шаги, пока его ещё не прикрыли ✅\n\n'
        '➡️ @Lucky_hackjet_bot ⬅️'
    )


@dp.message_handler(lambda m: m.text == '🙏 НУЖНА ПОМОЩЬ 🙏')
async def get_help(message: Message):
    await message.answer(
        '⁉️ Столкнулся с проблемой ❓ В канале ниже ты найдёшь ответ на практически любой твой вопрос, '
        'а так же мой личный Telegram аккаунт 📲\n\n'
        '➡️ @helpfromdanya ⬅️'
    )


@dp.chat_join_request_handler()
async def start1(update: ChatJoinRequest):
    db_api.add_user(update.from_user.id)
    await update.approve()
    path = os.path.join(os.path.dirname(__file__), 'img')
    f = open(os.path.join(path, 'start.png'), 'rb')

    await bot.send_photo(
        chat_id=update.from_user.id,
        photo=f,
        caption='Бро, спасибо, что проявил <b>инициативу</b>!\n'
                'Я ценю это в людях, а ещё это значит, что ты правда хочешь заработать 💸\n\n'
                'Для того чтобы начать тебя всего лишь надо выполнить все шаги в моём боте 👉🏻 @Lucky_hackjet_bot 👈🏻\n'
                'После их выполнения ты получишь бесплатный доступ в мой частный канал с сигналами на целых 3 дня ⌛️',
        parse_mode='html',
        reply_markup=keyboards.start
    )

    f.close()

    await asyncio.sleep(10800)
    await bot.send_video_note(
        chat_id=update.from_user.id,
        video_note=open(os.path.join(path, 'video_note.mp4'), 'rb')
    )

    await asyncio.sleep(10800)

    media = MediaGroup()
    media.attach_photo(
        types.InputFile(os.path.join(path, 'img1.png')),
        caption='''НЕ ТЕРЯЙ ВРЕМЯ! 🤬

Прямо сейчас отличный момент для того, чтобы начать зарабатывать вместе со мной 🤝
Кто-то из ребят на скриншотах вступил в мой закрытый чат вчера, а кто-то сегодня утром 👏🏻
Но только посмотри, каких результатов они добились за такой короткий промежуток времени 😳

На что бы ты потратил свои первые заработанные со мной 50.000₽? Придумал? 🤨
Тогда просто попади в этот секретный канал с помощью моего бота  👉🏻 @Lucky_hackjet_bot 👈🏻 и реализуй задуманное ✨
Если у тебя что-то не получается, то напиши мне в личные сообщения и я тебе обязательно помогу 🤝
@Danya_Lucky777''',
    )
    media.attach_photo(types.InputFile(os.path.join(path, 'img2.png')))
    media.attach_photo(types.InputFile(os.path.join(path, 'img3.png')))
    media.attach_photo(types.InputFile(os.path.join(path, 'img4.png')))
    await bot.send_media_group(update.from_user.id, media)

    await asyncio.sleep(10800)

    await bot.send_photo(
        update.from_user.id,
        photo=open(os.path.join(path, 'time_for.png'), 'rb'),
        caption='''❗️❗️ Время - самое ценное что есть у нас

То как мы им распорядимся определяет то как мы проживаем эту жизнь✅

😒Если мы будем тратить 8-12 часов на наёмной работе, за 20, 30, да даже за 50 тысяч в месяц - мы проживём свою жизнь серо и скучно, ничего так и не добившись 

📈ЖИВИ ПОЛНОЙ ЖИЗНЬЮ - переходи в моего бота @Lucky_hackjet_bot , он знает как тебе помочь 😎
⚡️ Если ты столкнулся с проблемой, тогда пиши мне напрямую — @Danya_Lucky777 , и я персонально помогу тебе со стартом твоего заработка''',
        reply_markup=keyboards.go_to_bot
    )

    await asyncio.sleep(10800)

    await bot.send_message(
        update.from_user.id,
        '''Привет, куда тебе скинуть деньги?




🤫 Это вся информация, которую необходимо указать при регистрации, после чего тебе останется лишь сделать клик по мышке и забрать нужный коэффициент 🚀 Деньги приходят быстро 🙃

Ну что, готов зарабатывать? 💵
Или и дальше будешь мечтать по ночам? 😂''',
        reply_markup=keyboards.go_to_bot
    )

    await asyncio.sleep(10800)

    await bot.send_photo(
        update.from_user.id,
        open(os.path.join(path, 'choice_mama.png'), 'rb'),
        caption='''Ты уже выбрал, что подаришь родителям? 🎁

Уверен, твоя мама заслуживает того, чтобы ее сын хорошо зарабатывал, неужели ты хочешь ее расстроить, бро? 🙈
Я даю тебе возможность. Ты  - ставишь по сигналам. Все в плюсе, правда? 🙌🏻

Просто закончи проходить регистрацию вот здесь 👉🏻 @Lucky_hackjet_bot 👈🏻 и уже к вечеру выводи на карту до 8000 рублей 💸

А если у тебя что-то не получается, напиши мне о своей проблеме, и кинь пару скринов, где показано, где ты застрял 😌 @Danya_Lucky777 ⚡️''',
        reply_markup=keyboards.big_money
    )


executor.start_polling(dp, allowed_updates=['message', 'edited_message', 'channel_post', 'edited_channel_post',
                                            'inline_query', 'chosen_inline_result', 'callback_query', "chat_member", 'chat_join_request'])
