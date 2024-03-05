from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from chatgpt_requests import ChatGptRequests

import loguru

chgptrouter = Router()
chatgptrequest = ChatGptRequests(proxy={})


@chgptrouter.message(Command('say'))
async def say(msg: Message):
    prompt = ' '.join(msg.text.split()[1:])
    try:
        msg = await msg.answer('⌛ Generate answer...')
        answer_async_gen = await chatgptrequest.generate_text(prompt)
        answer = ''

        for i in answer_async_gen:
            chunk = i.choices[0].delta.content
            if isinstance(chunk, str):
                answer += chunk
    except Exception as e:
        loguru.logger.error(e)
    else:
        await msg.edit_text(answer, parse_mode='Markdown')