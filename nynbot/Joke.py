import os
import random 
from openai import OpenAI

client = OpenAI(api_key="")
OPENAI_CHAT_MODEL = "gpt-3.5-turbo"



class Joke:
    @staticmethod
    def get_joke():
        response = client.chat.completions.create(model=OPENAI_CHAT_MODEL,
        messages=[
            {"role": "system", "content": "Tell me a joke."},
        ])