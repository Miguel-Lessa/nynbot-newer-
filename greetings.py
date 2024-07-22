
from datetime import datetime

class Greetings:
    @staticmethod
    def get_greeting():
        current_hour = datetime.now().hour

        if 6 <= current_hour < 12:
            return 'Bom dia! Que o seu dia seja ratástico!'
        elif 12 <= current_hour < 18:
            return 'Boa tarde! Você está quase lá!'
        elif 18 <= current_hour < 23:
            return 'Boa noite! Já está quase na hora de dormir!'
        else:
            return 'Já passou da hora de dormir! Já pra cama!'