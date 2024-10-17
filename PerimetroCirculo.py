diametro = 0
perimetro = 0
raio = 0
area = 0
pi = 3.14
perimetro = float(input('Informe o perímetro: '))
diametro = perimetro / pi
raio = diametro / 2
area = raio * raio / 2
print('O diâmetro é {}, o raio é {}, e a área é {}.'.format(diametro, raio, area))
