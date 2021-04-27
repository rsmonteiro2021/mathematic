"""
    Importa as funções do módulo right_triangle para calcular a área do triângulo retângulo
"""
import right_triangle

print('\nCalcula a área e a hipotenusa de um triângulo retângulo!')
base = int(input('Digite a base do triângulo retângulo:\nPara encerrar digite 0!\n'))

while base > 0:
    if base == 0:
        print('Programa encerrado com sucesso!')
        break
    altura = int(input('Digite a altura do triângulo retângulo:\n'))
    h = right_triangle.hipotenusa(base, altura)
    area_triangulo = right_triangle.area_triangulo_retangulo(base, altura)
    
    print(f'\nResposta:\n\tO triângulo retângulo de lados {base} e {altura} possui hipotenusa = {h} e área = {area_triangulo}\n')
    base = int(input('Digite a base do novo triângulo retângulo:\nPara encerrar digite 0!\n'))