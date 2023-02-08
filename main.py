import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import tokens

token = tokens.bot_token
openai.api_key = tokens.openAI_token

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.3,
        max_tokens=1500,
        top_p=0.3,
        frequency_penalty=0.0,
        presence_penalty=0.3,
        stop=[" Human:", " AI:"]
    )
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
