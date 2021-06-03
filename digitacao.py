print('#' * 120)
print('Jogo de digitação')
print('#' * 120)

import requests
import random
import time

url = 'https://www.mit.edu/~ecprice/wordlist.10000'

resposta = requests.get(url)
palavras = resposta.content.splitlines()

palavras = [palavra.decode('utf-8') for palavra in palavras]

random_palavras = random.sample(palavras, 10)

pontos = 0
inicio = time.perf_counter()

for palavra in random_palavras:
    print(palavra)
    entrada = input()
    if entrada == palavra:
        pontos += 1

termino = time.perf_counter()

print(pontos)
print(termino - inicio)

print('FIM DO PROGRAMA')