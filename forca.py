import random

def jogar():

    apresentacao()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print(f'Você errou, ainda tem {(6 - erros)} chances.')

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    
    if acertou:
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor(palavra_secreta)

def apresentacao():
    print('#' * 100)
    print('Bem vindo ao Jogo da Forca')
    print('#' * 100)

def carregar_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    # palavras = []
    # with open('palavras.txt') as arquivo:
    #     for linha in arquivo:
    #         linha = linha.strip()
    #         palavras.append(linha)

    numero = random.randrange(len(palavras))
    
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Digite uma letra.')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_mensagem_perdedor(palavra_secreta):
    print(f'Você foi enforcado! A palavra secreta era {palavra_secreta}.')

if __name__ == '__main__':
    jogar()