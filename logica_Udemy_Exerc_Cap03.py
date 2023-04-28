def exerc1():
    #Exercicio 1 - Ler as medidas da largura e comprimento de um terreno retangular com uma casa decimal, bem como o valor do metro quadrado do terreno com duas cassas decimais.
    #   Em seguida, o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com duas casas decimais.
    print(10 * '-' + 'Exercicio1' + '-' * 10 )
    largura = int(input('Digite a largura do terreno: '))
    comprimento = int(input('Digite o comprimento do terreno: '))
    valorM2 = float(input('Digite o valor do metro quadrado: ')) #-- M2 = M² = Metro quadrado
    area = largura * comprimento
    preco = valorM2 * area
    print(f'Area do terreno = {area:.2f}')
    print(f'Preço do terreno = {preco:.2f}')
    
def exerc2():
    #Exercicio 2 - Ler as medidas da base e altura de um retângulo.
    #   Em, seguida, mostrar o valor da área, perímetro e diagonal deste retângulo, com quatro casas decimais.
    b = float(input('Base do retângulo: '))   # base (b)
    h = float(input('Altura do retângulo: '))     # altura (h)
    area = b * h        # Calculo da base A = b * h
    perimetro = 2 * (b + h)   # Calculo do perimetro P = 2 ( b + h )
    diagonal = (b ** 2 + h ** 2) ** 0.5     # Calculo da diagonal d² = b² + h² => d= SQRT(b² + h²) | SQRT = Raiz Quadrada
    print(f'AREA = {area:.4f}')
    print(f'PERIMETRO = {perimetro:.4f}')
    print(f'DIAGONAL= {diagonal:.4f}')
    
def exerc3():
    #Exercicio 3 - Ler a idade de 2 pessoas. Ao final mostrar uma msg com os nomes e a idade média entre essas pessoas.
    nome_P1 = input('Dados da primeira pessoa\nNome: ')
    idade_p1 = int(input('Idade: '))
    nome_P2 = input('Dados da segunda pessoa\nNome: ')
    idade_p2 = int(input('Idade: '))
    media = (idade_p1 + idade_p2) / 2   # Cálculo da média = (X1 + X2 + ... + Xn) / n
    print(f'A idade media de {nome_P1} e {nome_P2} é de {media:.1f} anos')

def exerc4():
    #Exercicio 4 - SOMA Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes números.
    x = int(input('Digite o valor de X: '))
    y = int(input('Digite o valor de Y: '))
    soma = x + y
    print('SOMA = ', soma)

def exerc5():
    #Exercicio 5 - TROCO O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente).
    #   Seu programa deve mostrar o valor do troco a ser devolvido ao cliente. 
    prod1Preco = float(input('Preço unitário do produto: R$ '))
    prod1Qtd = float(input('Quantidade comprada: '))
    prod1Pagamento = float(input('Dinheiro recebido: R$ '))
    troco = float(prod1Pagamento - prod1Preco * prod1Qtd)
    print(f'TROCO = R$ {troco:.2f}')
    
def exerc6():
    #Exercício 6 - CIRCULO Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do círculo com três casas decimais. 
    #   A fórmula da área do círculo é a seguinte: 𝑎𝑟𝑒𝑎 = 𝜋 * r². 
    #   Você pode usar o valor de 𝜋 fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use diretamente o valor 3.14159. 
    PI = 3.14159    # Constante do valor de PI 
    r = float(input('Digite o valor do raio: '))
    area = PI * r * r    # Cálculo do raio de um círculo 𝑎𝑟𝑒𝑎 = 𝜋 * r² 
    print(f'Exerc6\n AREA = {area:.3f}')

def exerc7():
    #Exercício 7 - PAGAMENTO Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a quantidade de horas trabalhadas por ele(a). 
    #   Ao final, mostrar o valor do pagamento do funcionário com uma mensagem explicativa
    funcNome = input('Nome: ')
    valorH = float(input('Valor por hora: R$ '))
    funcHT = int(input('Horas trabalhadas(HT): '))
    pagamento = valorH * funcHT
    print(f'O pagamento para {funcNome} deve ser R$ {pagamento:.2f}')

def exerc8():
    #Exercicio 8 - CONSUMO Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de combustível gasto por este carro ao percorrer tal distância. 
    #   Seu programa deve mostrar o consumo médio do carro, com três casas decimais.
    S = int(input('Distância percorrida (km): '))   # Distância percorrida em quilômetros (S)
    v = float(input('Combustível gasto: '))     # Quantidade de combustível utilizada em litros (v)
    cM = S / v   # Razão do consumo médio(cM) = distancia percorrida(S) / quantidade combustivel gasto(v)
    print(f'Consumo médio = {cM:.3f} por litro')
    
def exerc9():
    #Exercício 9 - MEDIDAS Fazer um programa para ler três medidas A, B e C. 
    #   Em seguida, calcular e mostrar (imprimir os dados com quatro casas decimais): 
    #       a) a área do quadrado que tem lado A
    #       b) a área do triângulo retângulo que base A e altura B
    #       c) a área do trapézio que tem bases A e B, e altura C 
    A = float(input('Digite a medida A: ')) 
    B = float(input('Digite a medida B: '))
    C = float(input('Digite a medida C: '))
    areaQuadrado = A * A   # Cálculo da área do quadrado area = lado(A)² 
    areaTriangulo = 0.5 * A * B  # Cálculo da área do triângulo area = 0.5 * base(A) * altura(B)
    areaTrapezio = (A + B) * C * 0.5    # Cálculo da área do trapézio area = ((base Maior(A) + base Menor(B)) * altura(C)) / 2 => ((A+B)*C) * 0.5
    print(f'a). AREA DO QUADRADO = {areaQuadrado:.4f}\
          \nb). AREA DO TRIANGULO = {areaTriangulo:.4f}\
          \nc). AREA DO TRAPEZIO = {areaTrapezio:.4f}')

def exerc10(x):
    #Exercício 10 - DURAÇÃO Fazer um programa para ler uma duração de tempo em segundos, 
    #   daí imprimir na tela esta duração no formato horas:minutos:segundos.
    #   duracao = int(input('Digite a duração em segundos: '))
    # Infomação: Sabe-se 1min é = 60seg e 1h é = 60min

    duracao = x
    horas = duracao // 3600 # 1h = 3600seg
    minutos = (duracao % 3600) // 60 # 1min = Resto da divisão de duracao(segundos) por hora e dividido novamente por 60, q indica os minutos
    segundos = duracao % 60 # Resto da divisão de duracao(segundos) por 60, q indica os minutos
    print(f'{horas:.0f}:{minutos:.0f}:{segundos:.0f}')
#exerc10(300) #output 0:5:0
#exerc10(12506) #output 3:28:26 
#exerc10(140811) #output 39:6:51
#------------------- FIM ----------------

exerc10(3662)
exerc10(300) #output 0:5:0
exerc10(12506) #output 3:28:26 
exerc10(140811) #output 39:6:51

#soluções dos exercícios esperadas pelo professor: https://github.com/acenelio/curso-algoritmos/tree/master/visualg
