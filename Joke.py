import os
import random 

class Joke:
    @staticmethod
    def get_joke():
        random_number = random.randint(1, 3)
        if random_number == 1:
            return ('todo 1')        
        if random_number == 2:
            return ('to do 2')
        if random_number == 3:
            return ('to do 3')