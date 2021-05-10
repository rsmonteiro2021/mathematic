"""Calcula a área de uma figura geométrica regular (Quadrado, Retângulo, Losango, Triângulo Retângulo,
    Triângulo Isosceles, Triângulo Equilátero, Trapézio e Círculo):"""
# Autor: Roberto dos Santos Monteiro
# Upgrade em 10 de maio de 2021.

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
        """Retorna a hipotenusa de um triângulo retângulo"""
        import math
        a = math.sqrt(pow(self.base,2) + pow(self.altura,2))
        return a
    
    def area_triangulo_iso(self):
        """Retorna a área de um triângulo retângulo"""
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

class Trapezio():
    """Tentativa simples de modelar um trapézio."""
    
    def __init__(self, lado_maior, lado_menor, altura):
        """Inicializa os atributos dos trapézio."""
        self.lado_maior = lado_maior
        self.lado_menor = lado_menor
        self.altura = altura

    def trapezio_area(self):
        """Retorna a área do trapézio."""
        area = ((self.lado_maior + lado_menor) * altura)/2
        return area

while True:

    figuras = {'Quadrado': 1, 'Retângulo': 2, 'Triângulo': 3, 'Losango': 4, 'Trapézio': 5, 'Círculo': 6, 'Para Encerrar': 0}

    for figura, ordem in figuras.items():
        print(str(ordem) + ': ' + figura)

    figura = int(input('Que figura você deseja calcular a área?\n'))
    
    if figura == 0:
        print('\nObrigado por sua visita o Programa foi Encerrado. Espero ter ajudado.\n')
        break

    elif figura == 1:
        print('A figura escolhida é um quadrado.')
        base = float(input('Informe a medida do lado do quadrado em cm:\n'))
        altura = base
        geometria = Geomether(base, altura)
        geometria.quadrilatero()
        print('\n\t- O quadrado de lado = %5.2f tem área a = %5.2fcm².\n' % (base, geometria.quadrilatero()))

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
                print('\nResposta:')
                print('\n\t- O retângulo possui de lado = %5.2fcm, altura = %5.2fcm e área a = %5.2fcm².\n' % (base, altura, geometria.quadrilatero()))
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
                print('\nResposta:\n\t- O triângulo é equilátero (3 lados iguais), de lado L = %5.2fcm e área = a %5.2f cm².\n' % (lado, geometria.area_triangulo_iso()))
            else:
               print('\nResposta:zn\t- O triângulo é isósceles (2 lados iguais), de lado L1 = L2 = %5.2fcm, L3 = %5.2fcm e área = a %5.2f cm².' % (lado, lado_diferente, geometria.area_triangulo_iso()))
        elif tipo == 'L' or tipo == 'l':
            base = float(input('Você selecionou o triângulo Retângulo.\nDigite o valor de um dos catetos (cm):\n'))
            altura = float(input('Digite a medida do outro cateto em (cm):\n'))
            geometria = Geomether(base, altura)
            geometria.area_triangulo_retangulo()
            geometria.hipotenusa()
            print('\nResposta:\n\t-O triângulo possui cateto A = %5.2fcm, cateto B = %5.2fcm e hipotenusa = %5.2fcm, possui área a = %5.2fcm².\n' % (base, altura, geometria.hipotenusa(), geometria.area_triangulo_retangulo()))

    elif figura == 4:
        print('Você seleionou losango.')
        diagonal_1 = float(input('Digite a medida de uma das diagonais do losango (em cm):\n'))
        diagonal_2 = float(input('Digite a medida da outra diagonal do losango (em cm):\n'))
        losango = Losango(diagonal_1, diagonal_2)
        print('\nResposta\n\t- A área do losango de diagonais D1 = %5.2fcm e D2 = %5.2fcm é a = %5.2fcm²\n' % (diagonal_1, diagonal_2, losango.area_losango()))

    elif figura == 5:
        print('Você seleionou Trapézio.')
        lado_maior = float(input('Digite a medida do lado maior do Trapézio (em cm):\n'))
        lado_menor = float(input('Digite a medida do lado menor do Trapézio (em cm):\n'))
        altura = float(input('Digite a altura do Trapézio em cm:\n'))
        trapezio = Trapezio(lado_maior, lado_menor, altura)
        print('\nResposta:\n\t- A área do Trapézio de lados L1 = %5.2fcm e L2 = %5.2fcm e altura h = %5.2f é a = %5.2fcm²\n' % (lado_maior, lado_menor, altura, trapezio.trapezio_area()))
    
    elif figura == 6:
        raio = float(input('Você selecionou Círculo.\nDigite o raio do círculo:\n'))
        geometria = Geomether(0, 0, raio)
        print('\nResposta:\n\t- A área do círculo de raio = %5.2fcm é a = %5.2fcm².\n' % (raio, geometria.circulo()))
    
    else:
        print('\nERROR: Digite uma opção válida!\n')