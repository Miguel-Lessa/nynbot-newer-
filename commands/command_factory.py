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