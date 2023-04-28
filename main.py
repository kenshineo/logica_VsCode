import random 

print("Olá!")
# Execicio - Arquivo pattern.py
print("      1")
print("    2 3")
print("  4 5 6")
print("7 8 9 10")
# Execicio - Arquivo initials.py
# I guess I'm not very fun.
print('TTTTT   SSS    CCC   FFFFF')
print('  T    S   S  C   C  F')
print('  T    S      C      F')
print('  T     SSS   C      FFF')
print('  T        S  C      F')
print('  T    S   S  C   C  F')
print('  T     SSS    CCC   F')
# Execicio - Arquivo letter.py
#1.Today's date; 2.How you are feeling richt now; 3.What you want to accomplish during this course; 4.A little message to your older, wiser, and programmer self; 5.Your favorite emoji to spice things up!
print('1. 25/04/2023')
print('2. Estou me sentindo muito bem.')
print('3. Desejo aprender do básico ao avançado os conceitos de python.')
print('4. Queria uma ajuda para começar entrar no mercado de trabalho.')
print('5. 😎')
# Execicio - Arquivo temperature.py
#Crie um programa que converta uma temperatura de Fahrenheit para Celsius.
#Use a fórmula Celsius = (Fahrenheit - 32) / 1.8
fahren = 56
cels = (fahren - 32) / 1.8
print("-----------------\nCelsius para Fahrenheit\n-----------------")
print(f"{fahren}Fº = {cels:.1f}Cº\n-----------------")
# https://www.codedex.io/python/08-bmi -- 
# Execicio - Arquivo bmi.py
#Crie um programa que calcule o BMI, https://en.wikipedia.org/wiki/Body_mass_index
#Fórmula bmi = mass / height²
mass = 92.3
height = 1.86
bmi = mass / (height * height)
print(f"O calculo BMI para uma massa = {mass} e a altura {height}, BMI = {bmi}")
#Entrada de Dados
#Por padrão utiliza-se o objeto input para entrada de dados e o valor armazenado é do tipo string
#Exemplos de entradas convertidas para outros tipos de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá {nome}, sua idade é {idade} anos.")
print(f"O tipo da variável nome = {type(nome)} e o tipo da variável idade = {type(idade)}")
# Execicio - Arquivo hypotenuse.py
#Crie um programa que calcula o teorema da Hipotenusa, criado por Pitagoras, c = raiz(a²+b²)
a = 2
b = 3
c = 1
hipotenusa = (a*a + b*b) ** 0.5
print(f"O valor da Hipotenusa = {hipotenusa}")
x1 = ((-b) + ((b**2) - (4 * a * c)) ** 0.5) / (2 * a)
x2 = ((-b) - ((b**2) - (4 * a * c)) ** 0.5) / (2 * a)
print(f"O valor de x1 = {x1} e x2 = {x2}")
#Exercicio - Arquivo currency.py
#Criar um programa que pergunta o usuario o valor que ele tem em yuan, yen e won e mostra o montante somado e convertido para DOLAR.
yuan = float(input("Quanto você tem em yuan? "))
yen = float(input("Quanto você tem em yen? "))
won = float(input("Quanto você tem em won? "))
totalDolar = (yuan / 6.93) + (yen / 133.73 ) + (won / 1338.64)
#totalDolar = (yuan * 0.14) + (yen * 0.0075 ) + (won * 0.00075) - Resultado previsto
print(f"O valor somado e convertido em dolar é $ {totalDolar}")
#Exercicio - coin_flip.py
# Com uso da classe random, faça um programa que gere aleatoriamente um número inteiro entre 0 e 1 e após faça uma comparação se o número gerado é maior ou menor que 0.5, se for maior, imprima Heads, se for menor imprima Tails
num = random.randint(0, 1)
if num > 0.5:
    print('Heads')
else:
    print('Tails')
