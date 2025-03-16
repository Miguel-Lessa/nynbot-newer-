      
from commands.command import Command
from commands.greetings import Greetings
from discord import Message

class GreetCommand(Command):
    def __init__(self):
        self.greetings = Greetings()
        current_hour = datetime.now().hour
    async def execute(self, message: Message):
        await message.channel.send(self.greetings.get_greeting())