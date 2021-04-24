# Calcula a área de um triângulo Retângulo a partir das medidas dos catetos e retorna o valor da
# hipotenusa:
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

print('\nCalcula a área e a hipotenusa de um triângulo retângulo!')
base = int(input('Digite a base do triângulo retângulo:\nPara encerrar digite 0!\n'))
while base > 0:
    if base == 0:
        print('Programa encerrado com sucesso!')
        break
    altura = int(input('Digite a altura do triângulo retângulo:\n'))
    h = hipotenusa(base, altura)
    area_triangulo = area_triangulo_retangulo(base, altura)
    print(f'\nResposta:\n\tO triângulo retângulo de lados {base} e {altura} possui hipotenusa = {h} e área = {area_triangulo}\n')
    base = int(input('Digite a base do novo triângulo retângulo:\nPara encerrar digite 0!\n'))