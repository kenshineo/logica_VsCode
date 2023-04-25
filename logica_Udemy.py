#Logica Basica
#Variaveis
varInteiro = 10
varString = "Reiniciando a lógica!"
#Entrada - Atribuição INTERNA
print("Exemplos de variaveis recebendo atribuição interna:")
print(f"variavel Inteiro = {varInteiro}")
varInteiro = 5
print(f"Agora variavel Inteiro foi redefinida para = {varInteiro}")
#Entrada - Atribuição EXTERNA, do usuario para a maquina
#Neste exemplo o programa faz uma leitura do teclado e armazena em uma variável string de nome "nome1"
nome1 = input("Digite seu nome: ")
#Saida - Da maquina para o usuario
#Neste exemplo o progrma mostra na tela o conteúdo da variável "nome1"
print('-------------------------')
print(nome1)
print('-------------------------')
#Operações basicas entre variáveis
varInteiro = varInteiro + 10
n1 = 5
n2 = 10
n3 = 20
n4 = 2
n5 = 3
print(f"O valor da variavel varInteiro era 10 e depois de adicionados mais 10, ficou = {varInteiro}")
print(f"Iniciamos as variaveis n1, n2 e n3 com os valores {n1}, {n2} e {n3}")
#Adição +
print(f"Agora vamos somar {n1} + {n2} + {n3} = {n1 + n2 + n3}")
#Subtração -
print(f"Agora vamos subtrair {n3} - {n2} = {n3 - n2}")
#Multiplicação *
print(f"Agora vamos multiplicar {n1} * {n2} = {n1 * n2}")
#Divisão com resultado REAL /
print(f"Agora vamos dividir, resultado em REAL, {n3} / {n1} = {n3 / n1}")
#Divisão com resultado INTEIRO  //
print(f"Agora vamos dividir, resultado em INTEIRO, {n2} // {n1} = {n2 // n1}")
#Potencialização **
print(f"Agora vamos elevar {n5} ** {n4} = {n5 ** n4}")
#Exemplo de uma expressao numerica do calculo da area sendo b+B / 2 * h
b = 6.0
B = 8.0
h = 5.0
area = (b + B) / 2 * h
print(f"O calculo da area (b + B) / 2 * h, com os valores de b={b}, B={B} e h={h}, tem resultado = {area:.0f}")
#Passagem de valores entre variaveis de TIPOS diferentes
