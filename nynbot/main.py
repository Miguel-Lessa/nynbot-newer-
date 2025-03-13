import json 
import logging
import os 
import platform
import random
import sys
from typing import Final
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord import Client, File
from greetings import Greetings
from Joke import Joke
import sys
from io import BytesIO
from help import help
from meme import meme
from images import nsfw, safebooru, reisa
from games import vinte_um
      
greetings = Greetings() 
joke = Joke()
help = help()
meme = meme()

discord_intents: discord.Intents = discord.Intents.all()
discord_intents.message_content = True
client: Client = discord.Client(intents=discord_intents)

response_intents = {

}

@client.event
async def on_ready():
    channel = client.get_channel(YOUR_CHANNEL_ID)
    if channel:
        await channel.send("Bom dia sensei! Uzawa Reisa, ao seu dispor!:sparkles:")         

PREFIX = '%'

@client.event
async def on_message(message = discord.Message) -> None:
    if message.author == client.user:
        return None
    if not message.content.startswith(PREFIX):
        return None

    command = message.content[len(PREFIX):].lower()
    
#this will handle the chat requests
    match command:
        case 'hello':
            await message.channel.send(greetings.get_greeting())
        case 'help':
            await message.channel.send(help.get_help())
        case 'meme':
            await message.channel.send(meme.get_meme())
        case 'joke':
            await message.channel.send(joke.get_joke())
        case _ if command.startswith('image'):
            tags = command[len('image '):].strip()
            if tags:
                image_url = safebooru.get_random_image_url(tags)
                await message.channel.send('Here is the ' + tags + ' image you asked me to bring, sensei!:sparkles:')
                await message.channel.send(image_url)               
            else:
                await message.channel.send (':what:')
                await message.channel.send('What the sigma sensei! You need to provide me a tag!')
        case _ if command.startswith('você') and message.author.name == 'mikathesecond':                      
            await message.channel.send ('Hehe! Obrigada! Sensei!:heart:')
            
        case _ if command.startswith('hug'):
            if len(message.mentions) > 0:
                mentioned_user = message.mentions[0]
                hug_gif_url = "https://media.discordapp.net/attachments/1285272793432461485/1326254799414362194/Untitled.gif?ex=678602c8&is=6784b148&hm=00e177fc1fa465225a781da6c658663d5dc0ef9a658cc8d1c3a2ff70a6be1f31&=&width=399&height=223"
                await message.channel.send(f"> {message.author.mention} [hugged]({hug_gif_url}) {mentioned_user.mention}!:owl:")
            else :
                await message.channel.send("Sensei! Marque alguém que você queira :owl:")   
        case 'blackjack':
           await vinte_um(message)                      
        case 'skibidi':
            await message.channel.send ("Skibidi skibidi hawk tuah hawk, edging and gooning in ohio hawk tuah hawk!")
        case _ if command.startswith('te amo'):
            await message.channel.send ('Eu também te amo, sensei! :heart:')
                                    
                                                        
            
        
@client.event        
async def send_message(message: discord.Message, user_message: str) -> None:
    if not user_message:
        print ('Sai daqui glowie!')
        return
    if is_private := user_message [0] == '?':
        user_message = user_message [1:]
        
    try:
        response: str = get_response (user_message) # type: ignore
        await message.author.send if is_private else message.channel.send(response)    
    except Exception as e:
        print (e)

@client.event
async def on_ready():
    print('Bot positivo e operante')
    
client.run('')  