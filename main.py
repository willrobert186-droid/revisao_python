import random

opcoes = ['p', 'a', 't']

nome = input('Digite seu nome: ')

jogador = input('Escolha [p]edra, p[a]pel ou [t]esoura: ')
if jogador != 'p' and jogador != 'a' and jogador != 't':
    print('Você escolheu errado.')
else:
    computador = random.randrange(0,3)
    jogador = opcoes.index(jogador)
    print(f'computador: {opcoes[computador]}')
    print(f'jogador: {opcoes[jogador]}')

if computador == 0: # pedra
    if jogador == 1: #papel
        vencedor = 'jogador'
    elif jogador == 2: #tesoura
        vencedor = 'computador'
    else:
        vencedor = 'empate'
elif computador == 1: # papel
    if jogador == 0: #pedra
        vencedor = 'computador'
    elif jogador == 2: #tesoura
        vencedor = 'jogador'
    else:
        vencedor = 'empate'
else: # tesoura
    if jogador == 0: #pedra
        vencedor = 'jogador'
    elif jogador == 1: #papel
        vencedor = 'computador'
    else:
        vencedor = 'empate'

print(f'O vencedor é: {vencedor}')