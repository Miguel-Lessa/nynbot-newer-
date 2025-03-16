
import requests
from discord import File
from io import BytesIO
import random

class gear:
    @staticmethod
    def get_random_image_url():
        base_url = 'https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1'
        tags = 'nazrin'
        url = f'{base_url}&tags={tags}'

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        random_image_data = random.choice(data)
        image_url = f"https://safebooru.org/images/{random_image_data['directory']}/{random_image_data['image']}"
        return image_url
    
    
    @staticmethod
    async def send_random_image(message):
        image_url = Rato.get_random_image_url()
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        await message.channel.send(file=File(image_data, 'random_image.jpg'))
