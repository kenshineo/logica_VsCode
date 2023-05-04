#Logica Basica
import math

def primeirosPassos():
    #Variaveis
    varInteiro = 10
    varString = "Reiniciando a lógica!"
    #Entrada - Atribuição INTERNA
    print("Exemplos de variaveis recebendo atribuição interna:")
    print(f"variavel Inteiro = {varInteiro}")
    varInteiro = 5
    print(f"Agora variavel Inteiro foi redefinida para = {varInteiro}")
    #Entrada - Atribuição EXTERNA, ou LEITURA, acontece do usuario para a maquina
    #Neste exemplo o programa faz uma leitura do teclado e armazena em uma variável string de nome "nome1"
    nome1 = input("Digite seu nome: ")
    #Saida - Acontece da maquina para o usuario
    #Neste exemplo o progrma mostra na tela o conteúdo da variável "nome1"
    print('-------------------------')
    print(nome1)
    print('-------------------------')

def operacoes():
    #Operações basicas entre variáveis
    n1 = 5
    n2 = 10
    n3 = 20
    n4 = 2
    n5 = 3
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
    #Raiz função math.sqrt() ou x ** 0.5
    x = 25
    print(f'A raiz quadrada de {x} é {x**0.5}')
    #Valor absoluto de um número, exemplo: -5 = 5
    print(f'O valor absoluto de -1 = {abs(-1)}')
    #Valor de PI
    pi = math.pi
    print(f'O valor de PI = {pi}')


def calculoSeno():
    #Exemplo de uma expressao numerica do calculo da area sendo b+B / 2 * h
    b = 6.0
    B = 8.0
    h = 5.0
    area = (b + B) / 2 * h
    print(f"O calculo da area (b + B) / 2 * h, com os valores de b={b}, B={B} e h={h}, tem resultado = {area:.0f}")

def estructCondicionais():
    #CAPITOLO 04 - Estruturas Condicionais
    #Expressões comparativas
    x = 5
    print('EXPRESSOES COMPARATIVAS')
    print(f'Para x= {x}\nx é maior que 0 => {x > 0}')
    print(f'x é igual a 0 => {x == 0}')
    print(f'x é menor ou igual a 0 => {x <= 0}')
    print(f'x é diferente de 0 => {x != 0}')

    print('EXPRESSOES LOGICAS')
    print('Tabela VERDADE do operador E (AND)\nConsidere V= Verdadeiro e F= Falso')
    print('V AND V = ', True and True)
    print('V AND F = ', True and False)
    print('V AND F = ', False and True)
    print('F AND F = ', False and True)
    print('F AND F AND V = ', False and False and True)

    print('Tabela VERDADE do operador OU (OR)')
    print('V OR V = ', True or True)
    print('V OR F = ', True or False)
    print('F OR V = ', False or True)
    print('F OR F = ', False or False)

    print('Tabela VERDADE do operador NÃO (NOT)')
    print('Não V = ', not True)
    print('Não F = ', not False)
    print('Não V AND F = ', not (True and False))
    print('Não F AND F = ', not (False and False))
    print('Não V OU F = ', not (True or False))
    print('Não V OU V = ', not (True or True))
    
    #Estrutura condicional SIMPLES - SE (IF)
    #Conceito: if <condicao>:<comando> - Se a <condicao> for V então executa <comando>, caso contrário ignora <comando>
    print('Estrutura condicional SIMPLES - IF')
    if (x > 1):
        print(f'Neste caso x[{x}] é maior que 1') # Somente mostrado se o valor de x for maior que 1
    #Exemplo SAUDAÇÃO - Leia que horas são e:
    #  se for entre 0 e 12 mostre "Bom dia!"
    #  se for entre 13 e 18 mostre "Boa tarde!"
    #  se for entre 19 e 23 mostre "Boa noite!" 
    horario = int(input('Informe que horas são agora: (H) ')) 
    if ((horario >= 0) and (horario <=12)):
        print('Bom dia!')
    if ((horario >= 13) and (horario <=18)):
        print('Bom tarde!')
    if ((horario >= 19) and (horario <=23)):
        print('Bom noite!')
    #Estrutura condicional COMPOSTA - SENÃO (ELSE)
    #Conceito: Se não for satisfeito a primeira condição, então executa o segundo comando
    #   if <condicao>:
    #       <comando1>
    #   else:
    #       <comando2>
    # Se a <condicao> for V então executa <comando1>, caso contrário executa <comando2>
    x = 1
    print('Estrutura condicional COMPOSTA - IF ELSE')
    if x==1:
        print('Condição do SE, para x==1')
    else:
        print('Condição do SENÃO, para x==1')
    # Existe ainda a Estrutura condicional composta SENÃO SE (ELIF)
    #Conceito: Se não for satisfeito a condição1, então executa-se um novo teste com a condição2 e caso seja satisfeito, executa o comando2 porém se ainda não for satisfeito executa o comando3
    #   if <condicao1>:
    #       <comando1>
    #   elif <condicao2>:
    #       <comando2>
    #   else:
    #       <comando3>
    # Se a <condicao1> for V então executa <comando1>, caso contrário verifica <condicao2>, então se a 2 for V executa <comando2> e se for F executa o <comando3>
    print('Estrutura condicional COMPOSTA - IF ELIF ELSE')
    if x==1:
        print('Condição1 Verdadeira para x==1 ')
    elif x==2:
        print('Condição2 Verdadeira para x==2 ')
    else:
        print('SENÃO, onde x é diferente de 1 e de 2')

def estructCondEscolha():
    #Exemplo da estrutura condicional ESCOLHA
    #Está estrutura pré-determina a escolha com base no valor de uma variável, então ela direciona de forma condicional para um determinado valor, ou comando, de retorno
    escolha = int(input('Digite uma opção entre 1 a 7: '))
    dia = 'DIA'
    #Abaixo segue a estrutura do match-case:
    # match <variavel>:
    #   case <valor1>:
    #       <comando1>
    #   case <valor2>:
    #       <comando2>
    #   case <valor3>:
    #       <comando3>
    # Exemplo: 
    match escolha:
        case 1:
            dia = 'SEGUNDA'
        case 2:
            dia = 'TERÇA'
        case 3:
            dia = 'QUARTA'
        case 4:
            dia = 'QUINTA'
        case 5:
            dia = 'SEXTA'
        case 6:
            dia = 'SABADO'
        case 7:
            dia = 'DOMINGO'

    if escolha > 0 and escolha < 8:
        print(f'O dia escolhido foi {dia}')
    else:
        print('Opção inválida!')

def estructRepetitivas():
    #Estruturas repetitivas
    #WHILE (Enquanto) - É uma estrutura de controle que repete um bloco de comandos enquanto uma condição for verdadeira.
    #Ideal de se utilizar quando não se sabe previamente a quantidade de repetições que será realizada. 
    # while <condicao>:
    #   <comando>
    #Por exemplo, um programa que lê números até que o usuário digite 0 (ZERO).
    numero = 0
    qtdNumeros = 0
    primeiro = numero = int(input('Digite um número qualquer ou ZERO para SAIR: '))
    soma = 0
    ultimo = 0
    while numero != 0:
        soma += numero 
        numero = int(input('Digite um número qualquer ou ZERO para SAIR: '))
        if numero != 0:
            ultimo = numero
        qtdNumeros += 1
    print(f'O primeiro número digitado foi: {primeiro}')
    print(f'O último número digitado foi: {ultimo}')
    print(f'A soma de todos os números digitados é = {soma}')
    print(f'A quantidade de números digitados é = {qtdNumeros}')

estructRepetitivas()