import forca
import numero_secreto

print('#' * 100)
print('Escolha um jogo')
print('#' * 100)

while True:
    print('(1) Forca, (2)Numero secreto ou digite (s) para sair')

    jogo = int(input('Qual jogo deseja: '))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        numero_secreto.jogar()
    elif str(jogo.lower()) == 's':
        break