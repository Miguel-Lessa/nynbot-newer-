import os
from dotenv import load_dotenv
import discord
from commands.command_factory import CommandFactory

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

discord_intents: discord.Intents = discord.Intents.all()
discord_intents.message_content = True
client: discord.Client = discord.Client(intents=discord_intents)

PREFIX = '%'

@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return None
    if not message.content.startswith(PREFIX):
        return None

    command_type = message.content[len(PREFIX):].lower()
    try:
        command = CommandFactory.create_command(command_type)
        await command.execute(message)
    except ValueError as e:
        await message.channel.send(str(e))

@client.event
async def on_ready():
    print('Bot positivo e operante')

client.run(DISCORD_TOKEN)