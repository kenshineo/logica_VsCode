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
    somaIdades = 0
    n = 0
    media = 0.0
    idades = int(input('Digite as idades: '))
    if idades < 0:
        print('IMPOSSIVEL CALCULAR')
    else:
        while idades >= 0:
            n += 1
            media += idades
            idades = int(input('Digite as idades: '))

        media2 = media / n
        media /= n
        if n > 0:
            print(f'MEDIA = {media:.2f}')

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
    cordenadaX = 1
    cordenadaY = 1
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
    valor1 = float(input('Digite a primeira nota: '))
    while valor1 < 0 or valor1 > 10:
        valor1 = float(input('Valor inválido! Tente novamente: '))
    valor2 = float(input('Digite a segunda nota: '))
    while valor2 < 0 or valor2 > 10:
        valor2 = float(input('Valor inválido! Tente novamente: '))
    media = (valor1 + valor2) / 2    

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
    #Exercício 7 - PARES CPMSECUTIVOS - O  programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). 
    #   Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X, se for par. 
    #   Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, 
    #   por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
    x = int(input('Digite um número interiro: '))
    while x != 0:
        i = 0
        soma = 0
        while i < 5:
            if x % 2 == 0:
                soma += x
                x += 2
                i += 1        
            else:
                x += 1

        print(f'SOMA = {soma}, i = {i}, x = {x}')
        x = int(input('Digite um número interiro: '))

def exerc8():
    #Exercício 8 - TABUADA - Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10. 
    numero = int(input('Deseja a tabuada para qual valor? '))
    i = 1
    while i <= 10:
        print(f'{numero} x {i:2} = {numero * i}')
        i += 1

def exerc9():
    #Exercício 9 - SOMA IMPARES - Leia 2 valores inteiros X e Y (em qualquer ordem). 
    #   A seguir, calcule e mostre a soma dos números impares entre eles. 
    x = int(input('Digite o valor do número X: '))
    y = int(input('Digite o valor do número Y: '))
    i = impares = 0
    if x > y:
        diferenca = x - y
        p1 = x
    else:
        diferenca = y - x
        p1 = y

    print(f'X= {x} | Y= {y} | p1= {p1} | i = {i} | diferenca = {diferenca} | impares = {impares}')
    while i <= diferenca:
        if diferenca % 2 == 0:
            p1 -= 1
            i += 1
            print(f'X= {x} | Y= {y} | p1= {p1} | i = {i} | diferenca = {diferenca} | impares = {impares}')
        else:
            impares += p1
            p1 -= 2
            i += 1
            print(f'X= {x} | Y= {y} | p1= {p1} | i = {i} | diferenca = {diferenca} | impares = {impares}')

    print(f'SOMA DOS IMPARES = {impares}')
    print('Com DEFEITO')

exerc9()
