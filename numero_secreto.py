import random

class configuracoes:
    def __init__(self):
        self.nome = ''
        self.nivel = 0
        self.chute = 0
        self.pontos = 0
        self.chances = 0
        self.tentativas = 1
        self.numero_secreto = 0

    def apresentacao():
        print('O Jogo vai começar! Boa sorte!')
        print('Tente adivinhar o número secreto entre 1 e 100.')

    def nome_jogador(self):
        self.nome = input('Qual o seu nome? ')

    def escolha_nivel(self):
        nivel = int(input('Digite o nível de dificuldade para (1)Fácil, (2)Médio e (3)Difícil.'))
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

    def chute(self):
        while True:
            self.chute = int(input('Digite seu chute: '))
            if self.chute >= 1 and self.chute <= 100:
                break
            else:
                print('Número inválido! Digite um número entre 1 e 100')

    def ultimas_chances(self):
        if self.chances == 2:
            print('Jogue com atenção, só restam 2 chances')
        elif self.chances == 1:
            print('Arrisque toda sua sorte, é sua última chance.')
    
    def chances(self):
        self.chances -= 1

    def tentativas(self):
        self.tentativas += 1
        

def jogar():
    jogador = configuracoes()
    configuracoes.apresentacao()
    configuracoes.nome_jogador(jogador)
    configuracoes.escolha_nivel(jogador)
    configuracoes.numero_secreto(jogador)

    while jogador.chances > 0 and jogador.pontos > 0:
        
        configuracoes.chute(jogador)
        configuracoes.chances(jogador)
        configuracoes.tentativas(jogador)

        acertou = jogador.chute == jogador.numero_secreto
        maior = jogador.chute > jogador.numero_secreto
        menor = jogador.chute < jogador.numero_secreto

        if acertou:
            print (f'Parabéns! {jogador.nome} você acertou o número secreto ({jogador.numero_secreto}) com {jogador.tentativas} tentativas e fez {jogador.pontos} pontos.')
            break
        else:
            pontos_perdidos = abs(jogador.chute - jogador.numero_secreto)
            jogador.pontos -= pontos_perdidos
            if maior:
                print(f'Você errou, o número secreto é menor, ainda restam {jogador.chances} chances.')
            elif menor:
                print(f'Você errou, o número secreto é maior, ainda restam {jogador.chances} chances.')
            
        configuracoes.ultimas_chances(jogador)
        
    else:
        print(f'{jogador.nome} Você perdeu! O número secreto era ({jogador.numero_secreto})! Fim de jogo')

if __name__ == '__main__':
    jogar()