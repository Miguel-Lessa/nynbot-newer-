import os
import random 

class Joke:
    @staticmethod
    def get_joke():
        random_number = random.randint(1, 3)
        if random_number == 1:
            return ('Por que o peixe não gosta de água? Porque ele já bebeu demais')        
        if random_number == 2:
            return ('9')
        if random_number == 3:
            return ('eu vou te taxar')