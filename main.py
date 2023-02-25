# добавление бибилотек
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import tokens
import analytics as anly

a
token = tokens.bot_token
openai.api_key = tokens.openAI_token

bot = Bot(token)
dp = Dispatcher(bot)


# хендлер и вызов функции
@dp.message_handler()
@anly.analytics
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.4,
        max_tokens=2048,
        top_p=0.3,
        frequency_penalty=0.7,
        presence_penalty=0.3,
        stop=[" Human:", " AI:"]
    )
    
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
