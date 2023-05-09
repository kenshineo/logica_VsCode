def exerc1():
    #Exercício 1 - NEGATIVOS - Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros e armazene-os em um vetor. 
    #   Em seguida, mostrar na tela todos os números negativos lidos. 
    n = int(input('Quantos números você vai digitar? '))
    vetor = []
    for i in range(n):
        vetor.append(int(input('Digite um número: ')))
    print('Exercício 01 - NÚMEROS NEGATIVOS')
    for i in vetor:
        if i < 0:
            print(i)

def exerc2():
    #Exercício 2 - SOMA VETOR - Faça um programa que leia N números reais e armazene-os em um vetor. 
    #   Em seguida: - Imprimir todos os elementos do vetor; - Mostrar na tela a soma e a média dos elementos do vetor;
    n = int(input('Quantos números você vai digitar? '))
    vetor = []
    soma = 0.0
    print('Exercício 02 - SOMA VETOR')
    for i in range(n):
        vetor.append(float(input('Digite um número: ')))
        soma += vetor[i]
    media = soma / len(vetor) # ou media = soma / n pois n é a quantidade de itens do vetor
    print(f'VALORES = {vetor}')
    print(f'SOMA = {soma:.2f}\nMEDIA = {media:.2f}')

def exerc3():
    #Exercício 3 - ALTURAS - Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. 
    #   Depois, mostrar na tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos, bem como os nomes dessas pessoas caso houver. 
    print('Exercício 03 - ALTURAS')
    n = int(input('Quantas pessoas serão digitadas? '))
    menores = 0
    mediaAltura = somaAltura = 0.0
    vetorNome = []
    vetorIdade = []
    vetorAltura = []
    vetorMenores = []
    #Laço para leitura dos dados do usuário
    for i in range(n):
        print(f'Dados da {i + 1}ª pessoa: ')
        vetorNome.append(input('Nome: '))
        vetorIdade.append(int(input('Idade: ')))
        vetorAltura.append(float(input('Altura: ')))
    #Laço para calcular a soma das alturas e depois o calculo da media
    for i in range(n):
        somaAltura += vetorAltura[i]
    mediaAltura = somaAltura / n
    print(f'ALtura média: {mediaAltura:.2f}') # Resultado da média de altura
    #Laço para verificar as pessoas menores de 16 anos e o percentual que representa
    for i in range(n):
        if vetorIdade[i] < 16:
            vetorMenores.append(vetorNome[i])
            menores += 1
    percMenores = menores / n * 100 # Cálculo do percentual de menores
    print(f'Pessoas com menos de 16 anos: {percMenores:.1f} %') # Resultado da média das pessoas menores de 16
    #Laço para imprimir as pessoas Menores de 16
    for i in vetorMenores:
        print(i)

def exerc4():
    #Exercício - NUMEROS PARES - Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na tela todos os números pares, 
    #   e também a quantidade de números pares. 
    print('Exercício 04 - NUMEROS PARES')
    vetor = []
    vetorPares = []
    n = int(input('Quantos números você vai digitar? '))
    contador = 0
    #Laço para ler os valores
    for i in range(n):
        vetor.append(int(input('Digite um número: ')))
    #Laço para contar os pares
    for i in vetor:
        if i % 2 == 0:
            vetorPares.append(i)
            contador += 1
    print(f'NÚMEROS PARES: {vetorPares}')
    print(f'QUANTIDADE DE PARES = {contador}')
    

exerc4()