import discord
from discord import file
import random
                        
class meme:
    @staticmethod
    def get_meme():
        number = random.randint(1, 7)
        if number == 1:
            return 'https://cdn.discordapp.com/attachments/1083708074092666963/1265085298828902544/waru.mp4?ex=66a039ff&is=669ee87f&hm=a95a1d64f55f3360895881e52cf426de438b5cd11124d0d6452ec54db3a424b5&'
        elif number == 2:
            return 'https://cdn.discordapp.com/attachments/1083708074092666963/1265084641547780178/heart.mp4?ex=66a03962&is=669ee7e2&hm=8df15ca382dcb238fc392bbf6990ca1880f7b353fc20445617ed3b154bf5a6e2&'
        if number == 3:
            return 'https://cdn.discordapp.com/attachments/907336089797267502/1265425892386144327/NYN_Alleycat_Blues.mov?ex=66a17733&is=66a025b3&hm=de65e8374f79d3748b240e2f2d299e731a862ab3a2062a5e519920b32b38a26e&'  
        if number == 4:
            return 'https://cdn.discordapp.com/attachments/907336089797267502/1265426063526334504/video0-13-3.mp4?ex=66a1775c&is=66a025dc&hm=962ea911f58aa8337ff1d62e17c82e5eb72e72f21647a2c2ae12b0e6d367fcd3&' 
        if number == 5:
            return 'https://cdn.discordapp.com/attachments/1284891633585750016/1328442147795370065/youtube-9_O9aNSnIDs.mp4?ex=6786b7a9&is=67856629&hm=d13ea680609a8b9b7cd14c115039d172c3fd0f4633b08b7d94596cce4d64cc40&'   
        if number == 6:
            return 'https://media.discordapp.net/attachments/1284891633585750016/1328442067420057792/IMG-20250110-WA0188.jpg?ex=6786b796&is=67856616&hm=015ca8ee9911f8ae901155ae3cd4d23d43fd793e986d7cd3e9e260c551abe31b&=&format=webp&width=531&height=531'
        if number == 7:
            return 'https://cdn.discordapp.com/attachments/1284891633585750016/1329139800740991141/youtube-xpbsl0Ps9Gk.mp4?ex=67894166&is=6787efe6&hm=0b7a886a8b27492be4386ad6e3af5594245e69bf5f511bc78ce8ee45f7da6eae&'