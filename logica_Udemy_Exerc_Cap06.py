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
    mediaAltura = 0.0
    somaAltura = 0.0
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
    #Exercício 4 - NUMEROS PARES - Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na tela todos os números pares, 
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
    
def exerc5():
    #Exercício 5 - MAIOR POSIÇÃO - Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela o maior número do vetor (supor não haver empates). 
    #   Mostrar também a posição do maior elemento, considerando a primeira posição como 0 (zero). 
    n = int(input('Quantos números você vai digitar? '))
    vetor = []
    maior = 0.0
    posicao = 0
    print('EXERCICIO 5 - MAIOR POSIÇÃO')
    for i in range(n):
        vetor.append(float(input('Digite um número: ')))
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i

    print(f'MAIOR VALOR = {maior:.2f}')
    print(f'POSIÇÃO DO MAIOR VALOR = {posicao}')

def exerc6():
    #Exercício 6 - SOMA VETORES - Faça um programa para ler dois vetores A e B, contendo N elementos cada. 
    #   Em seguida, gere um terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. 
    #   Imprima o vetor C gerado.
    print('EXERCICIO 6 - SOMA VETORES')
    n = int(input('Quantos valores vai ter cada vetor? '))
    vetorA = []
    vetorB = []
    vetorSOMA = []
    for i in range(n):
        vetorA.append(int(input(f'Digite o {i + 1}º valor do vetor A: ')))
    for i in range(n):
        vetorB.append(int(input(f'Digite o {i + 1}º valor do vetor B: ')))
    for i in range(n):
        vetorSOMA.append(vetorA[i] + vetorB[i])
    print(f'VETOR RESULTANTE: {vetorSOMA}')

def exerc7():
    #Exercício 7 - ABAIXO DA MEDIA - Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. 
    #   Em seguida, mostrar na tela a média aritmética de todos elementos com três casas decimais. 
    #   Depois mostrar todos os elementos do vetor que estejam abaixo da média, com uma casa decimal cada. 
    print('EXERCICIO 7 - ABAIXO DA MEDIA')
    n = int(input('Quantos elementos vai ter o vetor? '))
    somatorio = 0.0
    vetor = []
    abaixoMedia = []
    for i in range(n):
        vetor.append(float(input('Digite um número: ')))
        somatorio += vetor[i]
    media = somatorio / n
    for i in vetor:
        if i < media:
            abaixoMedia.append(i)
    print(f'MEDIA DO VETOR = {media:.3f}')
    print(f'ELEMENTOS ABAIXO DA MEDIA: {abaixoMedia}')

def exerc8():
    #Exercício 8 - MEDIA PARES - Fazer um programa para ler um vetor de N números inteiros. 
    #   Em seguida, mostrar na tela a média aritmética somente dos números pares lidos, com uma casa decimal. 
    #   Se nenhum número par for digitado, mostrar a mensagem "NENHUM NUMERO PAR" 
    print('EXERCICIO 8 - MEDIA PARES')
    n = int(input('Quantos elementos vai ter o vetor? '))
    vetor = []
    somatorio = 0
    contador = 0
    for i in range(n):
        vetor.append(int(input('Digite um número: ')))
        if vetor[i] % 2 == 0:
            somatorio += vetor[i]
            contador += 1
    if contador > 0:
        media = somatorio / contador
        print(f'MEDIA DOS PARES = {media:.1f}')
    else:
        print('NENHUM NÚMERO PAR')

def exerc9():
    #Exercício 9 - MAIS VELHO - Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. 
    #   Os nomes devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome da pessoa mais velha. 
    print('EXERCÍCIO 9 - MAIS VELHO')
    n = int(input('Quantas pessoas você vai digitar? '))
    v_PessoasNome = []
    v_PessoasIdade = []
    maisVelho = ''
    maior = 0
    for i in range(n):
        print(f'Dados da {i + 1}º pessoa:')
        v_PessoasNome.append(input('Nome: '))
        v_PessoasIdade.append(int(input('Idade: ')))
        if v_PessoasIdade[i] > maior:
            maior = v_PessoasIdade[i]
            maisVelho = v_PessoasNome[i]
    print(f'PESSOA MAIS VELHA: {maisVelho}')

def exerc10():
    #Exercício 10 - APROVADOS - Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram no 1º e 2º semestres. 
    #   Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir os nomes dos alunos aprovados, 
    #   considerando aprovados aqueles cuja média das notas seja maior ou igual a 6.0 (seis). 
    print('EXERCÍCIO 10 - APROVADOS')
    n = int(input('Quantos alunos serão digitados? '))
    v_Nomes = []
    v_NotaA = []
    v_NotaB = []
    v_Aprovados = []
    for i in range(n):
        v_Nomes.append(input('Digite o nome do aluno: '))
        v_NotaA.append(float(input('Primeira nota: ')))
        v_NotaB.append(float(input('Segunda nota: ')))
        media = (v_NotaA[i] + v_NotaB[i]) / 2
        print(f'MEDIA = {media}')
        if media >= 6.0:
            v_Aprovados.append(v_Nomes[i])
    print('ALUNOS APROVADOS')
    for i in v_Aprovados:
        print(i)

def exerc11():
    #Exercício 11 - DADOS PESSOAS - Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. 
    #   Fazer um programa que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número de homens. 
    print('EXERCÍCIO 11 - DADOS PESSOAS')
    n = int(input('Quantas pessoas serão digitadas? '))
    v_Altura = []
    v_Genero = []
    menorALtura = 1000.0
    maiorALtura = 0.0
    contadorFem = 0
    contadorMas = 0
    somaAltMulher = 0.0
    for i in range(n):
        v_Altura.append(float(input(f'Altura da {i + 1}º pessoa: ')))
        v_Genero.append(input(f'Gênero da {i + 1}º pessoa: '))
        if v_Genero[i] == 'm':
            contadorMas += 1
        else:
            contadorFem += 1
            somaAltMulher += v_Altura[i]
        if v_Altura[i] > maiorALtura:
            maiorALtura = v_Altura[i]
        if v_Altura[i] < menorALtura:
            menorALtura = v_Altura[i]
    mediaAlturaMulher = somaAltMulher / contadorFem
    print(f'Menor Altura = {menorALtura:.2f}')
    print(f'Maior Altura = {maiorALtura:.2f}')
    print(f'Media das alturas das mulheres = {mediaAlturaMulher:.2f}')
    print(f'Número de homens = {contadorMas}')
    

def exerc12():
    #Exercício 12 - COMERCIANTE - Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. 
    #   Para isto, mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de venda das mesmas. 
    #   Fazer um programa que leia tais dados e determine e escreva quantas mercadorias proporcionaram: 
    #       - lucro < 10% 
    #       - 10% ≤ lucro ≤ 20%  
    #       - lucro > 20%  
    #   Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como o lucro total.
    print('EXERCÍCIO 12 - COMERCIANTE')
    n = int(input('Serão digitados dados de quantos produtos? '))
    v_produtoNome = []
    v_precoCompra = []
    v_precoVenda = []
    totalCompra = 0.0
    totalVenda = 0.0
    lucroAbaixo10 = 0
    lucroAcima20 = 0
    lucroEntre10e20 = 0
    for i in range(n):
        print(f'Produto {i + 1}')
        v_produtoNome.append(input('Nome: '))
        v_precoCompra.append(float(input('Preço de compra: R$ ')))
        totalCompra += v_precoCompra[i]
        v_precoVenda.append(float(input('Preço de venda: R$ ')))
        totalVenda += v_precoVenda[i]
        lucro = (v_precoVenda[i] / v_precoCompra[i] - 1) * 100
        if lucro < 10:
            lucroAbaixo10 += 1
        elif lucro > 20:
            lucroAcima20 += 1
        else:
            lucroEntre10e20 += 1
    lucroTotal = totalVenda - totalCompra
    print('RELATORIO')
    print(f'Lucro abaixo de 10% {lucroAbaixo10}')
    print(f'Lucro entre 10% e 20% {lucroEntre10e20}')
    print(f'Lucro acima de 20% {lucroAcima20}')
    print(f'Valor total de compra: R$ {totalCompra:.2f}')
    print(f'Valor total de venda: R$ {totalVenda:.2f}')
    print(f'Lucro total R$ {lucroTotal:.2f}')

exerc12()
