#Lista de exercícios 
#CAPITULO 05 - Estruturas Repetitivas
def exerc1():
    #Exercício 1 - CRESCENTE - Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. 
    #   Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
    #   O programa deve finalizar quando forem digitados dois valores iguais.
    print('Digite dois números')
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    while num1 != num2:
        if num1 > num2:
            print('DECRESCENTE!')
        else:
            print('CRESCENTE!')
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))

def exerc2():
    #Exercício 2 - MEDIA IDADES - Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
    #   O último dado, que não entrará nos cálculos, contém um valor de idade negativa. 
    #   Calcular e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, mostrar a mensagem "IMPOSSIVEL CALCULAR".
    n = soma = 0
    media = 0.0
    idades = int(input('Digite as idades: '))
    while idades >= 0:
        n += 1
        soma += idades
        idades = int(input('Digite as idades: '))
    if n > 0:
        media = soma / n
        print(f'MEDIA = {media:.2f}')
    else:
        print('IMPOSSIVEL CALCULAR')

def exerc3():
    #Exercício 3 - SENHA FIXA - Escreva um programa que repita a leitura de uma senha até que ela seja válida. 
    #   Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". 
    #   Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. 
    #   Considere que a senha correta é o valor 2002.
    SENHA_CORRETA = 2002
    senha = int(input('Digite a senha: '))
    while senha != SENHA_CORRETA:
        senha = int(input('Senha Inválida! Tente novamente: '))
    print('Acesso Permitido!')

def exerc4():
    #Exercício 4 - QUADRANTE - Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. 
    #   Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA.
    #  (nesta situação sem escrever mensagem alguma)
    cordenadaY = cordenadaX = 1
    quadrante = ''
    while cordenadaX != 0 and cordenadaY != 0:
        cordenadaX = int(input('Digite o valor da coordenada X: '))
        cordenadaY = int(input('Digite o valor da coordenada Y: '))        
        if cordenadaX != 0 and cordenadaY != 0:        
            if cordenadaX > 0 and cordenadaY > 0:
                quadrante = 'Q1'
            elif cordenadaX < 0 and cordenadaY > 0:
                quadrante = 'Q2'
            elif cordenadaX < 0 and cordenadaY < 0:
                quadrante = 'Q3'
            elif cordenadaX > 0 and cordenadaY < 0:
                quadrante = 'Q4'
            print(f'QUADRANTE {quadrante}')

def exerc5():
    #Exercício 5 - VALIDAÇÃO DE NOTA - Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. 
    #   Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente. 
    media = 0.0
    for i in range(2):
        valor1 = float(input('Digite a primeira nota: '))
        while valor1 < 0 or valor1 > 10:
            valor1 = float(input('Valor inválido! Tente novamente: '))
        valor2 = float(input('Digite a segunda nota: '))
        while valor2 < 0 or valor2 > 10:
            valor2 = float(input('Valor inválido! Tente novamente: '))
        media = (valor1 + valor2) / 2
        i += 1
        print(f'MEDIA = {media:.2f}')

def exerc6():
    #Exercício 6 - COMBUSTÍVEL - Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
    #   Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). 
    #   Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). 
    #   O programa será encerrado quando o código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem como as quantidades de cada combustível. 
    codigo = alcool = gasolina = diesel = 0
    while codigo != 4:
        codigo = int(input('Informe um código (1, 2, 3) ou 4 para parar: '))
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1
    print('MUITO OBRIGADO')
    print(f'Alcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')

def exerc7():
    #Exercício 7 - PARES CONSECUTIVOS - O  programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). 
    #   Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X, se for par. 
    #   Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, 
    #   por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
    x = int(input('Digite um número interiro: '))
    while x != 0:
        soma = 0
        for i in range(5):
            if x % 2 == 0:
                soma += x
                x += 2
            else:
                x += 1
        print(f'SOMA = {soma}, i = {i}, x = {x}')
        x = int(input('Digite um número interiro: '))

def exerc8():
    #Exercício 8 - TABUADA - Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10. 
    numero = int(input('Deseja a tabuada para qual valor? '))
    for i in range(10):
        i += 1
        produto = i * numero
        print(f'{numero} x {i:2} = {produto}')

def exerc9():
    #Exercício 9 - SOMA IMPARES - Leia 2 valores inteiros X e Y (em qualquer ordem). 
    #   A seguir, calcule e mostre a soma dos números impares entre eles. 
    x = int(input('Digite o valor do número X: '))
    y = int(input('Digite o valor do número Y: '))
    acumulador = 0
    #Verificando qual dos dois termos é o maior para definir a ordem crescente obrigatoriamente, sendo X o menor e Y o maior
    if x > y:
        aux = x
        x = y
        y = aux
    x += 1
    y -= 1
    while x <= y:
        if x % 2 != 0:
            acumulador += x
        x += 1
    print(f'SOMA DOS IMPARES = {acumulador}')

def exerc10():
    #Exercício 10 - SEQUENCIA IMPARES - Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
    x = int(input('Digite o valor de X: '))
    for i in range(x):
        if (i + 1) % 2 != 0:
            print(i + 1)
        i += 1
        
def exerc11():
    #Exercício 11 - DENTRO FORA - Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida. 
    #   Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo.
    qtdNum = int(input('Quantos números você vai digitar? '))
    dentro = fora = 0
    for i in range(qtdNum):
        num = int(input('Digite um número: '))
        if num >= 10 and num <= 20:
            dentro += 1
        else:
            fora += 1
    print('VERIFICANDO QUANTOS DOS NÚMEROS DIGITADOS ESTÃO DENTRO DO INTERVALO [10,20]')
    print(f'{dentro} DENTRO')
    print(f'{fora} FORA')

def exerc12():
    #Exercício 12 -  PAR IMPAR - Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida. 
    #   Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também se é POSITIVO ou NEGATIVO. 
    #   No caso do valor ser igual a zero (0), seu programa deverá imprimir apenas NULO. 
    qtdNum = int(input('Quantos números você vai digitar? '))
    for i in range(qtdNum):
        num = int(input('Digite um número: '))
        if num == 0:
            print('NULO')
        elif num > 0:
            if num % 2 == 0:
                print('PAR POSITIVO')
            else:
                print('IMPAR POSITIVO')
        else:
            if num % 2 == 0:
                print('PAR NEGATIVO')
            else:
                print('IMPAR NEGATIVO')
        
def exerc13():
    #Exercício 13 - MEDIA PONDERADA - Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. 
    #   Cada caso de teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo que o primeiro valor tem peso 2, 
    #   o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, 
    #   dividida pela soma dos pesos.
    n = int(input('Quantos casos você vai digitar? '))
    PESO1 = 2
    PESO2 = 3
    PESO3 = 5
    for i in range(n):
        print('Digite três números: ')
        valor1 = float(input())
        valor2 = float(input())
        valor3 = float(input())
        mediaPonderada = (valor1 * PESO1 + valor2 * PESO2 + valor3 * PESO3) / (PESO1 + PESO2 + PESO3)
        print(f'MEDIA = {mediaPonderada:.1F}')

def exerc14():
    #Exercício 14 - DIVISAO - Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo segundo. 
    #   Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.
    n = int(input('Quantos casos você vai digitar? '))
    for i in range(n):
        numerador = int(input('Entre com o numerador: '))
        denominador = int(input('Entre com o numerador: '))
        if denominador == 0:
            print('DIVISÃO IMPOSSÍVEL!')
        else:
            divisao = numerador / denominador
            print(f'DIVISÃO {divisao:.2f}')

def exerc15():
    #Exercício 15 - FATORIAL - Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o fatorial de N. 
    n = int(input('Digite o valor de N: '))
    fatorial = 1
    for i in range(n):
        fatorial *= (i + 1)
    print(f'FATORIAL = {fatorial}')

def exerc16():
    #Exercício 16 - EXPERIÊNCIAS - Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. 
    #   Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. 
    #   Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento. 
    #   Faça um programa que leia um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), 
    #   indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, 
    #   sendo que o percentual deve ser apresentado com dois dígitos após o ponto. 
    n = int(input('Quantos casos de teste serão digitados: '))
    ratos = sapos = coelhos = 0
    for i in range(n):
        cobaias = int(input('Quantidade de cobaias: '))
        tipo = input('Tipo de cobaia [C-Coelho | R-Rato | S-Sapo]: ').upper()
        match tipo:
            case 'R':
                ratos += cobaias
            case 'S':
                sapos += cobaias
            case 'C':
                coelhos += cobaias
        total_cobaias = ratos + sapos + coelhos
    perc_coelhos = (coelhos / total_cobaias) * 100
    perc_ratos = (ratos / total_cobaias) * 100
    perc_sapos = (sapos / total_cobaias) * 100
    print('RELATÓRIO FINAL:')
    print(f'Total: {total_cobaias} cobaias')
    print(f'Total de coelhos: {coelhos}')
    print(f'Total de ratos: {ratos}')
    print(f'Total de sapos: {sapos}')
    print(f'Percentual de coelhos: {perc_coelhos:.2f}')
    print(f'Percentual de ratos: {perc_ratos:.2f}')
    print(f'Percentual de sapos: {perc_sapos:.2f}')


exerc16()
