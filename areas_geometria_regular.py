"""Calcula a área de uma figura geométrica regular (Quadrado, Retângulo, Losango, Triângulo Retângulo,
    Triângulo Isosceles, Triângulo Equilátero e Círculo):"""
# Autor: Roberto dos Santos Monteiro
# Upgrade em 08 de maio de 2021.

class Geomether():
    """Tentativa simples de modular o cálculo da área de uma figura geométrica regular"""
    def __init__(self, base, altura, raio=0):
        """Inicializa os atributos de uma figura geométrica regular."""
        self.base = base
        self.altura = altura
        self.raio = raio

    def quadrilatero(self):
        """Retorna a área de um quadrilátero."""
        area = self.base * self.altura
        return area
    
    def circulo(self):
        """Retorna a área de um círculoo."""
        import math
        area = math.pi * pow(self.raio, 2)
        return area
             
    def area_triangulo_retangulo(self):
        """Devolve a área de um triângulo retângulo"""
        area = self.base * self.altura/2
        return area
    
    def hipotenusa(self):
        """Devolve a hipotenusa de um triângulo retângulo"""
        import math
        a = math.sqrt(pow(self.base,2) + pow(self.altura,2))
        return a
    
    def area_triangulo_iso(self):
        """Devolve a área de um triângulo retângulo"""
        import math
        self.base = self.base
        area = (self.base * self.altura/2) * 2
        return area

class Losango():
    """Tentativa simples de modelar um losango."""
    def __init__(self, diagonal_1, diagonal_2):
        """Inicializa os atributos de um losango."""
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2
    def area_losango(self):
        """Retorna a área de um losango"""
        area = self.diagonal_1 * self.diagonal_2/2
        return area

figuras = {'Quadrado': 1, 'Retângulo': 2, 'Triângulo': 3, 'Losango': 4, 'Círculo': 5}

for figura, ordem in figuras.items():
    print(str(ordem) + ': ' + figura)

figura = int(input('Que figura você deseja calcular a área?\n'))

if figura == 1:
    print('A figura escolhida é um quadrado.')
    base = float(input('Informe a medida do lado do quadrado em cm:\n'))
    altura = base
    geometria = Geomether(base, altura)
    geometria.quadrilatero()
    print('O quadrado de lado = %5.2f tem área a = %5.2fcm².' % (base, geometria.quadrilatero()))

elif figura == 2:
    while True:
        base = float(input('Você selecionou o Retângulo.\nDigite o valor da base:\n'))
        altura = float(input('Digite o valor da altura do retângulo:\n'))
        if base == altura:
            print('ERROR:Um retângulo não possui medidas dos lados iguais! Digite os valores corretos!')
            continue
        else:
            geometria = Geomether(base, altura)
            geometria.quadrilatero()
            print('O retângulo possui de lado = %5.2fcm, altura = %5.2fcm e área a = %5.2fcm².' % (base, altura, geometria.quadrilatero()))
            break
    
elif figura == 3:
    tipos = {'Triâgulo Retângulo': 'L', 'Triângulo Isosceles': 'I'}
    print('Você pode escolher entre:')
    for triangulo, tipo in tipos.items():
        print('\t' + triangulo + ': ' + tipo)
    tipo = input('Digite o tipo de triangulo que deseja calcular a área:\n')
    if tipo == 'I' or tipo == 'i':
        lado = float(input('Você selecionou o triângulo isosceles.\nDigite o valor dos lados iguais em (cm):\n'))
        lado_diferente = float(input('Digite o valor da medida do lado diferente em (cm):\n'))
        base = lado_diferente/2
        import math
        altura = math.sqrt(pow(lado, 2) - pow(base, 2))
        geometria = Geomether(base, altura)
        geometria.area_triangulo_iso()
        if lado == lado_diferente:
            print('Resposta:')
            print('O triângulo é equilátero (3 lados iguais), de lado L = %5.2fcm e área = a %5.2f cm².' % (lado, geometria.area_triangulo_iso()))
        else:
            print('Resposta:')
            print('O triângulo é isósceles (2 lados iguais), de lado L1 = L2 = %5.2fcm, L3 = %5.2fcm e área = a %5.2f cm².' % (lado, lado_diferente, geometria.area_triangulo_iso()))
    elif tipo == 'L' or tipo == 'l':
        base = float(input('Você selecionou o triângulo Retângulo.\nDigite o valor de um dos catetos (cm):\n'))
        altura = float(input('Digite a medida do outro cateto em (cm):\n'))
        geometria = Geomether(base, altura)
        geometria.area_triangulo_retangulo()
        geometria.hipotenusa()
        print('Resposta:')
        print('O triângulo possui cateto A = %5.2fcm, cateto B = %5.2fcm e hipotenusa = %5.2fcm, possui área a = %5.2fcm².' % (base, altura, geometria.hipotenusa(), geometria.area_triangulo_retangulo()))

elif figura == 4:
    print('Você seleionou losango.')
    diagonal_1 = float(input('Digite a medida de uma das diagonais do losango (em cm):\n'))
    diagonal_2 = float(input('Digite a medida da outra diagonal do losango (em cm):\n'))
    losango = Losango(diagonal_1, diagonal_2)
    print('A área do losango de diagonais D1 = %5.2fcm e D2 = %5.2fcm é a = %5.2fcm²' % (diagonal_1, diagonal_2, losango.area_losango()))

elif figura == 5:
    raio = float(input('Você selecionou Círculo.\nDigite o raio do círculo:\n'))
    geometria = Geomether(0, 0, raio)
    print('A área do círculo de raio = %5.2fcm é a = %5.2fcm².' % (raio, geometria.circulo()))