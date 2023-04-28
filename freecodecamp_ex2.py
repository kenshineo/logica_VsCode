#https://www.freecodecamp.org/portuguese/news/25-projetos-em-python-para-iniciantes-ideias-faceis-para-comecar-a-programar-em-python/#projetos-em-python-que-voc-pode-criar
#Projeto n2 - Crie um algoritmo onde o PC gera um número secreto e nós tentamos advinhar qual é esse número
import random
n_scret = random.randint(0,9)
nome = input("Digite seu nome: ")
palpite = int(input("Digite um palpite: "))
if palpite == n_scret:
    print(f"Olá {nome}, você acertou!")
else:
    print(f"Olá {nome}, você errou!")
print(f"Número SESCRETO = {n_scret}")