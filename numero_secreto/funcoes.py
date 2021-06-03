import random

class configuracoes:
    def __init__(self):
        self.jogador = ''
        self.nivel = 0
        self.chute = 0
        self.tentativas = 1
        self.pontos = 0
        self.chances = 0
        self.numero_secreto = 0

    def apresentacao():
        print('O Jogo vai começar! Boa sorte!')
        print('Tente adivinhar o número secreto entre 1 e 100.')

    def nome_jogador(self):
        self.jogador = input('Qual o seu nome?')

    def escolha_nivel(self):
        nivel = int(input('Digite o nível de dificuldade para Fácil(1), Médio(2) e Difícil(3).'))
        if nivel == 1:
            self.chances = 12
            self.pontos = 120
        elif nivel == 2:
            self.chances = 8
            self.pontos = 90
        else:
            self.chances = 5
            self.pontos = 60

    def numero_secreto(self):
        numero_secreto = random.randint(1, 100)
        # numero_secreto = round(random.random() * 100)
        # numero_secreto = random.randrange(1, 101)
        self.numero_secreto = numero_secreto

