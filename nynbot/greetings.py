
from datetime import datetime

class Greetings:
    @staticmethod
    def get_greeting():
        current_hour = datetime.now().hour

        if 6 <= current_hour < 14:
            return ':sparkles:'
        elif 14 <= current_hour < 18:
            return ':sparkles:'
        elif 18 <= current_hour < 23:
            return ''
        else:
            return 'It is already past your bedtime!'