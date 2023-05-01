def exerc1():
    #Exercício 1 - NOTAS - Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de uma disciplina anual. 
    #   Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no ano juntamente com um texto explicativo. 
    #   Caso a nota final do aluno seja inferior a 60.00, mostrar a mensagem "REPROVADO"
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    notaFinal = nota1 + nota2
    if notaFinal < 60:
        print(f'NOTA FINAL = {notaFinal:.1f}\nREPROVADO')
    else:
        print(f'NOTA FINAL = {notaFinal}')

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


exerc3()
