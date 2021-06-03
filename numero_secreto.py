import random

def jogar():
    print('O Jogo vai começar! Boa sorte!')
    jogador = input('Qual o seu nome?')
    nivel = int(input('Digite o nível de dificuldade para Fácil(1), Médio(2) e Difícil(3).'))
    print('Digite um número entre 1 e 100.')

    chute = 0
    tentativas = 1
    pontos = 0
    chances = 0

    if nivel == 1:
        chances = 12
        pontos = 120
    elif nivel == 2:
        chances = 8
        pontos = 90
    else:
        chances = 5
        pontos = 60

    numero_secreto = random.randint(1, 100)
    # numero_secreto = round(random.random() * 100)
    # numero_secreto = random.randrange(1, 101)

    while tentativas <= chances and pontos > 0:
        while True:
            chute = int(input('Digite um número: '))
            if chute >= 1 and chute <= 100:
                break
            else:
                print('Número inválido! Digite um número entre 1 e 100')
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print (f'Parabéns! {jogador} você acertou o número secreto ({numero_secreto}) com {tentativas} tentativas e fez {pontos} pontos.')
            break
        else:
            pontos_perdidos = abs(chute - numero_secreto)
            pontos -= pontos_perdidos
            if maior:
                print(f'Você errou, o número secreto é menor, ainda restam {tentativas} / {chances} chances.')
            elif menor:
                print(f'Você errou, o número secreto é maior, ainda restam {tentativas} / {chances} chances.')

        penultima_chance = tentativas == chances - 2
        ultima_chance = tentativas == chances - 1
        if penultima_chance:
            print('Você tem mais 2 chances')
        elif ultima_chance:
            print('Você só tem essa chance')

        tentativas += 1
    else:
        print(f'{jogador} Você perdeu! O número secreto era ({numero_secreto})! Fim de jogo')

if __name__ == '__main__':
    jogar()