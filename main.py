# добавление бибилотек
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import tokens
import analytics as anly


token = tokens.bot_token
openai.api_key = tokens.openAI_token

bot = Bot(token)
dp = Dispatcher(bot)


# хендлер для "/start"
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name},'
                         f' чем могу помочь?')


# хендлер и вызов функции
@dp.message_handler()
@anly.analytics
async def send(message: types.Message):

    if message.text == "Привет!" or message.text == "Привет":
        await message.answer(
            f'Здравствуйте {message.from_user.first_name}!'
        )

    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0,
            max_tokens=2048,
            top_p=0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=[" Human:", " AI:"]
        )

        await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
