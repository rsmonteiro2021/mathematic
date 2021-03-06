# Módulo que define as funções 'area_triangulo' e 'hipotenusa' para calcular a área de um triângulo Retângulo:
# autor: Roberto dos Santos Monteiro

def area_triangulo_retangulo(base, altura):
    """Devolve a área de um triângulo retângulo"""
    area = base * altura/2
    return area
def hipotenusa(base, altura):
    """Devolve a hipotenusa de um triângulo retângulo"""
    import math
    a = math.sqrt(pow(base,2) + pow(altura,2))
    return a
