#https://www.freecodecamp.org/portuguese/news/25-projetos-em-python-para-iniciantes-ideias-faceis-para-comecar-a-programar-em-python/#projetos-em-python-que-voc-pode-criar
#Projeto n4 - Crie um algoritmo onde o PC gera um número secreto e nós tentamos advinhar qual é esse número
import random

def adivinhe_User(x):
    n_scret = random.randint(1,x)
    nome = input("Digite seu nome: ")
    palpite = 0
    n = 0
    while palpite != n_scret:
        n += 1
        palpite = int(input(f"Digite um palpite entre 1 e {x}: "))
        if palpite < n_scret:
            print(f"Tentativa {n} - Olá {nome} você errou! - Dica: Ta frio!")
        elif palpite > n_scret:
            print(f"Tentativa {n} - Olá {nome} você errou! - Dica: Ta quente!")

    print(f"Tentativa {n} - Parabéns {nome}, você acertou! O número SESCRETO é ({n_scret})")

def adivinhe_PC(x):
    min = 1
    max = x
    n = 0
    confere = ''
    while confere != 'c':
        palpite = random.randint(min, max)
        confere = input(f"O número {palpite} é maior(H) ou menor(L) ou está correto(C)?").lower()         
        if confere == 'h':
            max = palpite - 1
        elif confere == 'l':
            min = palpite + 1
        n += 1

    print(f" Tentativa {n} - O PC acertou! O número SESCRETO é {palpite}")

adivinhe_PC(1000)