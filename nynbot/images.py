
import requests
from discord import File
from io import BytesIO
import random                   

class safebooru:
    @staticmethod
    def get_random_image_url(tags):
        base_url = 'https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1'
        tags = tags
        url = f'{base_url}&tags={tags}'

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        random_image_data = random.choice(data)
        image_url = f"https://safebooru.org/images/{random_image_data['directory']}/{random_image_data['image']}"
        return image_url
    
    
class reisa:
    @staticmethod
    def get_random_image_url():
        base_url = 'https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1'
        tags = 'reisa_(blue_archive)'
        url = f'{base_url}&tags={tags}'

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        random_image_data = random.choice(data)
        image_url = f"https://safebooru.org/images/{random_image_data['directory']}/{random_image_data['image']}"
        return image_url

class nsfw:
    @staticmethod
    def get_random_image_url(tags):
        base_url = 'https://gelbooru.com/index.php?page=post&s=list&tags='
        tags = tags
        url = f'{base_url}&tags={tags}'

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        random_image_data = random.choice(data)
        image_url = f"https://gelbooru.com/index.php?page=post&s=list&tags={tags}"
        return image_url
    


        