import forca
import numero_secreto
import digitacao
import jo_ken_po

print('#' * 100)
print('Escolha um jogo')
print('#' * 100)

while True:
    print('Digite para (1) Forca, (2) Numero secreto, (3) Digitação, (4) Jo-ken-pô ou (0) zero para sair')

    jogo = int(input('Qual jogo você quer: '))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        numero_secreto.jogar()
    elif jogo == 3:
        digitacao.jogar()
    elif jogo == 4:
        jo_ken_po.jogar()
    elif jogo == 0:
        break