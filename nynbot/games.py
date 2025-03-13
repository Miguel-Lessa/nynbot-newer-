import random

async def vinte_um(message):
    total = 0
    active = True
    while total <= 21 and active:
        novaCarta = random.randint(1, 10)
        total += novaCarta
        await message.channel.send(f'Você tirou um {novaCarta} e está com {total}. Deseja pegar mais uma carta? (sim/não)')
        
        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            response = await client.wait_for('message', check=check, timeout=30.0)
            command = response.content.lower()
        except asyncio.TimeoutError:
            await message.channel.send('Tempo esgotado! Jogo encerrado.')
            break

        if command == 'sim':
            active = True
        elif command == 'não' or command == 'nao':
            if 18 <= total <= 21:
                await message.channel.send('Parabéns! Você ganhou! :sparkles:')
            else:
                await message.channel.send('Sinto muito... Mas você perdeu...')
            break
        if total > 21:
            await message.channel.send("Sinto muito, mas você estourou!")
            break