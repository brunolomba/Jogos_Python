import requests
import random
import time

def jogar():
    print('#' * 120)
    print('Jogo de digitação')
    print('#' * 120)

    url = 'https://www.mit.edu/~ecprice/wordlist.10000'

    resposta = requests.get(url)
    palavras = resposta.content.splitlines()

    palavras = [palavra.decode('utf-8') for palavra in palavras]

    random_palavras = random.sample(palavras, 10)

    acertos = 0
    inicio = time.perf_counter()

    for palavra in random_palavras:
        print(palavra)
        while True:
            entrada = input()
            if len(entrada) > 1:
                break
        if entrada == palavra:
            acertos += 1
        

    termino = time.perf_counter()

    print(f' Você acertou {acertos} palavras')
    if acertos == 10:
        print(f'Seu tempo foi de {termino - inicio} segundos')

    print('FIM DO PROGRAMA')

if __name__== '__main__':
    jogar()