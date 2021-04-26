# Resolução de Função do Segundo Grau Completa:
# ax2 + bx + c = y

print('Solução reais de funções do primeiro e do segundo grau. Entre com os dados da função:\n')

a = float(input('Digite o coeficiente angular da equação:\n'))
b = float(input('Digite o coeficiente linear da equação:\n'))
c = float(input('Digite o termo independente:\n'))
solucoes = {}

if a == 0:
    print("A equação é do primeiro grau!")
    # Função do primeiro grau:
    # bx + c = y
    y = 0.0
    x = -c/b
    print(f'Sua raíz é P({x}, {y}).')
else:
# Cálculo da Raíz da função do segundo grau:
    y = 0
# Veriricar o Delta:
    delta = (b**2) - (4 * a * c)
    if delta == 0:
        x1 = (-b/(2*a))
        x2 = x1
        solucoes.update({x1: y})
    elif delta < 0:
        print('A equação não possui raízes Reais!')
    else:
        x1 = ((-b + (delta**0.5))/(2*a))
        x2 = ((-b - (delta**0.5))/(2*a))
        solucoes.update({x1: y})

# Ponto de interceptação da equação com a reta y:

yi = c
xi = 0
solucoes.update({xi: yi})

# Cálculo do ponto mínimo ou máximo:
# O ponto mínimo ou máximo de uma função do segundo grau ocorre quando sua derivada da função em relação a x é igual a 0, portanto:
# f = ax2 + bx + c; f' = 2ax + b = 0

xm = (-b/(2*a))
ym = ((a*((xm)**2)) + (b*xm) + c)
solucoes.update({xm: ym})
if delta >= 0:
    print(f'As raízes da função foram calculadas e serão mostradas no final do programa.')
# para deteminar outros valores de y entre com o valor de x
s = 's'
while True:
    if s == 'n':
        break
    x = float(input('Entre com um valor para x, para determnar um valor para f(x)\n'))
    y = ((a*(x**2)) + (b*x) + c)
    solucoes.update({x:y})
    while True:
        s = input('Deseja determinar outro valor para f(x) (s/n)?\n')
        if s == 'n':
            break
        elif s == 's':
            s = True
            break
        else:
            print('Verifique a opção digitada, digite apenas s ou n!')

print('\nSoluções da função:')
print('Valores calculados:')
for x, y in solucoes.items():
    print(f'\tx= {x},  y= {y}')
print('\nOBSERVAÇÕES:')
if delta >= 0:
    print('\nAs raízes da função são:')
    if delta == 0:
        print('\t1 - As raízes da função são iguais - x1 = x2')
        print(f'\t\tx1 = x2 = {x1}')
    elif delta > 0:
        print('\t1 - A função possui raízes reais distintas.')
        print(f'\t\tx1 = {x1} e x2 = {x2}')
else:
    print('\t1 - A função não possui raízes reais!')
if a > 0:
    print(f'\t\t2 - O ponto mínimo da equação é Pmin = ({xm}, {ym})')
elif a < 0:
    print('\t2 - A parábola possui concavidade voltada para baixo, logo a função possui valor máximo.')
    print(f'\t\tO ponto máximo da equação é Pmax = ({xm}, {ym})')
print(f'\t3 - O ponto em que a curva intercepta a reta y é f(0) = ({xi}, {yi})')
