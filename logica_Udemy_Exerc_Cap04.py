def exerc1():
    #Exercício 1 - NOTAS - Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de uma disciplina anual. 
    #   Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no ano juntamente com um texto explicativo. 
    #   Caso a nota final do aluno seja inferior a 60.00, mostrar a mensagem "REPROVADO"
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    notaFinal = nota1 + nota2
    print(f'NOTA FINAL = {notaFinal}')
    if notaFinal < 60:
        print('REPROVADO')

def exerc2():
    #Exercicio 2 - BASKARA - Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula de Baskara, 
    #   calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais, conforme exemplo. 
    #   Se a equação não possuir raízes reais, mostrar uma mensagem. 
    # BASKARA x = -b ± SQRT(DELTA) / 2a
    # DELTA = b² - 4ac
         
    a = float(input('Coeficiente a: '))
    b = float(input('Coeficiente b: '))
    c = float(input('Coeficiente c: '))
    delta = b * b - 4 * a * c   # Este é o calculo do DELTA
    if delta < 0 or a == 0:
        print('DELTA menor que ZERO não possui resultados reais')
    else:
        print('DELTA maior que ZERO')
        x1 = (- b + (delta ** 0.5)) / (2 * a)
        x2 = (- b - (delta ** 0.5)) / (2 * a)    
        print(f'DELTA = {delta}\nX1 = {x1:.4f}\nX2 = {x2:.4f}')

def exerc3():
    #Exercicio 3 - MENOR DE 3 - azer um programa para ler três números inteiros. 
    #   Em seguida, mostrar qual o menor dentre os três números lidos. Em caso de empate, mostrar apenas uma vez. 
    valor1 = 1
    while valor1 > 0:
        print('Digite 3 valores e descrubra o MENOR valor - (0) ZERO para encerrar!')
        valor1 = int(input('Primeiro valor: '))
        if valor1 != 0:
            valor2 = int(input('Segundo valor: '))
            valor3 = int(input('Terceiro valor: '))
            if valor1 < valor2 and valor1 < valor3:
                print(valor1)
            else:
                if valor2 > valor3:
                    print(valor3)
                else:
                    print(valor2)

def exerc4():
    #Exercicio 4 - OPERADORA - Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de telefone. 
    #   Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. 
    #   Fazer um programa para ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago. 
    plan_Basic = 50.00
    valor_min_Extra = 2.00
    franquia = 100
    valor = plan_Basic
    qtd_Min_Gastos = int(input('Digite a quantidade de minutos: '))
    
    if qtd_Min_Gastos > franquia:
        valor += ((qtd_Min_Gastos - franquia) * valor_min_Extra)

    print(f'Valor a pagar: R$ {valor:.2f}')

def exerc5():
    #Exercício 5 - TROCO VERIFICADO - Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. 
    #   O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, e o valor em dinheiro dado pelo cliente. 
    #   Seu programa deve mostrar o valor do troco a ser devolvido ao cliente. 
    #   Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o valor restante conforme exemplo. 
    preco = float(input('Preço unitário do produto: R$ '))
    quantidade = int(input('Quantidade comprada: '))
    dinheiro_recebido = float(input('Dinheiro recebido: R$ '))
    totalCompra = preco * quantidade
    troco = dinheiro_recebido - totalCompra
    if totalCompra > dinheiro_recebido:
        print(f'DINHEIRO INSUFICIENTE. FALTAM R$ {abs(troco):.2f}')
    else:
        print(f'TROCO = R$ {troco:.2f}')

def exerc6():
    #Exercício 6 - GLICOSE - Fazer um programa para ler a quantidade de glicose no sangue de uma pessoa 
    #   e depois mostrar na tela a classificação desta glicose de acordo com a tabela de referência ao lado. 
    # |-----------------------------------------------|
    # |- CLASSIFICACAO  | GLICOSE                    -|
    # |-----------------------------------------------|
    # |- Normal         | Até 100 mg/dl              -|
    # |- Elevado        | Maior q 100 até 140 mg/dl  -|
    # |- Diabetes       | Maior de 140 mg/dl         -|
    # |-----------------------------------------------|
    medida_glicose = float(input('Digite a medida da glicose: '))
    if medida_glicose <= 100:
        situacao = 'Normal'
    elif medida_glicose <= 140:
        situacao = 'Elevado'
    else:
        situacao = 'Diabetes'

    print(f'Classificação: {situacao}')

def exerc7():
    #Exercício 7 - DARDO - No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir. 
    #   Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual foi a maior.
    print('Digite as tres distâncias')
    maior = 0
    distancia1 = float(input('1º: '))
    distancia2 = float(input('2º: '))
    distancia3 = float(input('3º: '))
    if distancia1 > distancia2 and distancia1 > distancia3:
        maior = distancia1
    elif distancia2 > distancia3:
        maior = distancia2
    else:
        maior = distancia3
    
    print(f'MAIOR DISTÂNCIA = {maior}')

def exerc8():
    #Exercício 8 - TEMPERATURA - Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. 
    #   Para isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser informada uma temperatura.
    #   Em seguida o programa deve mostrar a temperatura na outra escala com duas casas decimais. 
    #   A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve deduzir a fórmula de Celsius para Fahrenheit): C = 5/9 (F - 32)
    op_escala = input('Você vai digitar a temperatura em qual escala (C / F)? ')
    match op_escala:
        case 'c':
            valor_temperatura = float(input('Digite a temperatura em Celsius: '))
            temperatura = 9 * valor_temperatura / 5 + 32
            op_escala = 'Fahrenheit'
        case 'f':
            valor_temperatura = float(input('Digite a temperatura em Fahrenheit: '))
            temperatura = 5 / 9 * (valor_temperatura - 32)
            op_escala = 'Celsius'

    print(f'Temperatura equivalente em {op_escala}: {temperatura:.2f}')

def exerc9():
    #Exercício 9 - Uma lanchonete possui vários produtos. Cada produto possui um código e um preço. 
    #   Você deve fazer um programa para ler o código e a quantidade comprada de um produto (suponha um código válido), e daí informar qual o valor a ser pago, 
    #   com duas casas decimais, conforme tabela de produtos.
    # |-----------------------------|
    # |- CODIGO  | PREÇO PRODUTO   -|
    # |-----------------------------|
    # |-  1      | R$ 5.00         -|
    # |-  2      | R$ 3.50         -|
    # |-  3      | R$ 4.80         -|
    # |-  4      | R$ 8.90         -|
    # |-  5      | R$ 7.32         -|
    # |-----------------------------|
    codigo = int(input('Código do produto comprado: '))
    quantidade = int(input('Quantidade comprada: '))

    match codigo:
        case 1:
            valor = 5.00
        case 2:
            valor = 3.50
        case 3:
            valor = 4.80
        case 4:
            valor = 8.90
        case 5:
            valor = 7.32

    total = valor * quantidade
    print(f'Valor a pagar: R$ {total:.2f}')

def exerc10():
    #Exercício 10 - MULTIPLOS - Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. 
    #   Os números podem ser digitados em qualquer ordem. 
    print('Digite dois números inteiros')
    num1 = int(input('1º Número: '))
    num2 = int(input('2º Número: '))
    if num1 % num2 == 0 or num2 % num1 == 0:
        print('São multiplos')
    else:
        print('Não são multiplos')

def exerc11():
    #Exercício 11 - AUMENTO - Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto cada pessoa ganha, conforme tabela.
    #   Fazer um programa para ler o salário de uma pessoa, daí mostrar qual o novo salário desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento. 
    # |------------------------------|
    # |  Salário atual    | Aumento -|
    # |------------------------------|
    # |  Até 1000         | 20%     -|
    # |  De 1000 até 3000 | 15%     -|
    # |  De 3000 até 8000 | 10%     -|
    # |  Acima de 8000    |  5%     -|
    # |------------------------------|
    salario = float(input('Digite o salário da pessoa: R$ '))
    if salario <= 1000.00:
        porcentagem = 20
    elif salario <= 3000.00:
        porcentagem = 15
    elif salario <= 8000.00:
        porcentagem = 10
    else:
        porcentagem = 5
        
    aumento = salario * porcentagem / 100
    salarioNovo = salario + aumento
    print(f'Novo salário = R$ {salarioNovo:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print(f'Porcentagem = {porcentagem} %')

def exerc12():
    #Exercício 12 - TEMPO DE JOGO - Leia a hora inicial e a hora final de um jogo. 
    #   A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
    hInicial = int(input('Hora inicial: '))
    hFinal = int(input('Hora final: '))
    if hFinal <= hInicial:
        duracao = 24 - hInicial + hFinal
    else:
        duracao = hFinal - hInicial
    print(f'O JOGO DUROU {duracao} HORA(S)')

def exerc13():
    #Exercício 13 - COORDENADAS - Leia os valores das coordenadas X e Y de um ponto no plano cartesiano. 
    #   A seguir, determine qual o quadrante ao qual pertence o ponto (Q1, Q2, Q3 ou Q4). 
    #   Se o ponto estiver na origem, escreva a mensagem “Origem”. Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação. 
    x = float(input('Valor de X: '))
    y = float(input('Valor de Y: '))
    if x > 0 and y > 0:
        quadrante = 'Q1'
    elif x < 0 and y > 0:
        quadrante = 'Q2'
    elif x < 0 and y < 0:
        quadrante = 'Q3'
    elif x > 0 and y < 0:
        quadrante = 'Q4'
    elif x == 0 and y == 0:
        quadrante = 'Origem'
    elif x == 0:
        quadrante = 'Eixo Y'
    else:
        quadrante = 'Eixo X'
    
    print(quadrante)

exerc1()
