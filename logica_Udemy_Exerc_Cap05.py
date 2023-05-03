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
    print('Exercício 2')

exerc2()
