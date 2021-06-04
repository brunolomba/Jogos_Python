from random import choice

def jogar():
    
    apresentacao()
    jogo = config()
    visualizacao_escolha_computador(jogo)
    resultado(jogo)
    
####################################################################################################################################
class config:
    def __init__(self):
        self.lista = ['pedra', 'papel', 'tesoura']
        self.escolha = input('Digite para escolher: "pedra", "papel" ou "tesoura": ')
        self.escolha_computador = choice(self.lista)
        
def apresentacao():
    print('#' * 22)
    print('PEDRA, PAPEL e TESOURA')
    print('#' * 22)

def visualizacao_escolha_computador(self):
    print(f'O computador escolheu {self.escolha_computador}.')

def resultado(self):
    if self.escolha == 'pedra' and self.escolha_computador == 'papel':
        print('Você perdeu!')
    elif self.escolha == 'pedra' and self.escolha_computador == 'tesoura':
        print('Você Ganhou!')
    elif self.escolha == 'papel' and self.escolha_computador == 'tesoura':
        print('Você perdeu!')
    elif self.escolha == 'papel' and self.escolha_computador == 'pedra':
        print('Você Ganhou!')
    elif self.escolha == 'tesoura' and self.escolha_computador == 'pedra':
        print('Você perdeu!')
    elif self.escolha == 'tesoura' and self.escolha_computador == 'papel':
            print('Você Ganhou!')
    else:
        print('Empate!')

if __name__== '__main__':
    jogar()