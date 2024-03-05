from g4f.client import Client
from g4f import models
from g4f.Provider import You
from g4f.client import Proxies

import nest_asyncio

nest_asyncio.apply()


class ChatGptRequests:
    def __init__(self, proxy: str = None) -> None:
        self.client = Client(proxies=proxy)

    async def generate_text(self, prompt: str):
        response = self.client.chat.completions.create(
            model=models.gpt_4_turbo,
            messages=[{'role': 'user', 'content': prompt}],
            provider=You,
            stream=True,
        )
        return response
    
    async def generate_image(self, prompt: str):
        pass