print('#' * 120)
print('PEDRA, PAPEL e TESOURA')
print('#' * 120)

from random import choice

escolha = input('Digite "pedra", "papel" ou "tesoura" :')
lista = ['pedra', 'papel', 'tesoura']
escolha_computador = choice(lista)
print(f'O computador escolheu {escolha_computador}.')

if escolha == 'fechar':
    print('FIM DE JOGO')
elif escolha == 'pedra' and escolha_computador == 'papel':
    print('Você perdeu!')
elif escolha == 'pedra' and escolha_computador == 'tesoura':
    print('Você Ganhou!')
elif escolha == 'papel' and escolha_computador == 'tesoura':
    print('Você perdeu!')
elif escolha == 'papel' and escolha_computador == 'pedra':
    print('Você Ganhou!')
elif escolha == 'tesoura' and escolha_computador == 'pedra':
    print('Você perdeu!')
elif escolha == 'tesoura' and escolha_computador == 'papel':
        print('Você Ganhou!')
else:
    print('Empate!')