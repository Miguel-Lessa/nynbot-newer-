from commands.command import Command
from discord import Message
import random

class BlackjackCommand(Command):
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    def draw_card(self):
        return random.choice(self.deck)

    async def execute(self, message: Message):
        player_hand = [self.draw_card(), self.draw_card()]
        dealer_hand = [self.draw_card(), self.draw_card()]

        player_score = sum(player_hand)
        dealer_score = sum(dealer_hand)

        result = f"Your hand: {player_hand} (Total: {player_score})\n"
        result += f"Dealer's hand: {dealer_hand} (Total: {dealer_score})\n"

        if player_score > 21:
            result += "You bust! Dealer wins."
        elif dealer_score > 21 or player_score > dealer_score:
            result += "You win!"
        elif player_score < dealer_score:
            result += "Dealer wins."
        else:
            result += "It's a tie!"

        await message.channel.send(result)
        from commands.greet_command import GreetCommand
        from commands.joke_command import JokeCommand
        from commands.image_command import ImageCommand
        from commands.blackjack_command import BlackjackCommand
        
        class CommandFactory:
            @staticmethod
            def create_command(command_type):
                if command_type == 'ola':
                    return GreetCommand()
                elif command_type == 'joke':
                    return JokeCommand()
                elif command_type == 'image':
                    return ImageCommand()
                elif command_type == 'blackjack':
                    return BlackjackCommand()
                else:
                    raise ValueError(f"Unknown command type: {command_type}")
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