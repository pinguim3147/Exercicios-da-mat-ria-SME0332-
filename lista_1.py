"""" Ex.1: Faça um programa que dado um numero x, onde 1000 ≤ x < 10000, imprima o numero x com seus dígitos na ordem inversa.
Por exemplo: x = 2736, a resposta será 6372. """

a = input()
print(a[::-1])


""" Ex.2: Faça um programa que dada uma palavra, transforme todas suas letras em letras minúsculas.
Exceto a letra 'a', que ocorrera sempre 3 vezes na palavra, que devem ficar maiusculas. """

#esse código serve para casos em que 'a' repete mais de 3 vezes também

print(input().lower().replace('a','A'))


""" Ex.3: Faça um programa que dada a expressão algébrica de uma equação do segundo grau, troque x por y e
vice versa.
A equação sempre estará disposta na forma:
 y=ax2+bx+c """
 
 equacao = input().lower().replace('x','y').split('=')
print("x =" + equacao[1])


""" Ex.4: Dados dois vetores em R3, dados como entrada na forma: x1, y1, z1 e x2, y2, z2.
Onde x1, y1 e z1 são as coordenadas do primeiro vetor, e x2, y2 e z2 são as coordenadas do segundo vetor.
Calcule:

A soma entre eles;
O produto escalar;
O produto vetorial. """

x1, y1, z1 = [float(i) for i in input().split()]
x2, y2, z2 = [float(i) for i in input().split()]

#soma
xs = x1 + x2
ys = y1 + y2
zs = z1 + z2

#produto escalar
d = (x1 * x2) + (y1 * y2) + (z1 * z2)

#produto vetorial
xc = (y1*z2) - (y2*z1)
yc = (-1)*((x1*z2)-(x2*z1))
zc = (x1*y2) - (x2*y1)

print("%.2f" %xs ,"%.2f" %ys ,"%.2f" %zs ,)
print("%.2f" %d)
print("%.2f" %xc ,"%.2f" %yc ,"%.2f" %zc ,)


"""Ex.5:Faça um programa que transforme uma temperatura fornecida em Fahrenheit para a correspondente em Celsius.
A formula de conversão de Fahrenheit para Celsius é a seguinte: C= 59 ∗ (F–32)."""

fahrenheit = float(input())
celsius = ((5/9)*( fahrenheit -32))

print("%.2f" %celsius)


"""Ex.7:Escreva um programa que transforme o valor correspondente a um intervalo temporal, 
expresso em horas, minutos e segundos, no valor correspondente em segundos.

Entrada:

HH:MM:SS
Saída:

total_segundos"""

horas, minutos,segundos = input().split(':')
total_segundos = int((3600*float(horas)) + (60*float(minutos)) + float(segundos))

print(total_segundos)


"""Ex.8 Faça um programa que informe a distância em quilômetros de um raio para o observador.
O observador deve informar o tempo (em segundos) transcorrido entre ver o raio e ouvir o trovão.
Assuma que a velocidade do som seja 340m/s.
Entrada:
t

Saída:
d """

tempo = float(input())
distancia = ((tempo*340)/1000)
print("%.2f" %(distancia))


"""Ex.9: Faça um programa que, dada uma aceleração constante em m/s2 e o tempo de aceleração em segundos, calcule a distância em metros percorrida em uma pista para que um avião em repouso decole.

Entrada:
aceleracao tempo

Saída:
distancia """

aceleracao,tempo = input().split()
distancia =((float(aceleracao)*(float(tempo)*float(tempo)))/2)
print( "%.2f" % (distancia))


"""Ex.10:Seguindo a ideia da decolagem de um avião inicialmente em repouso. Faça um programa que dada a velocidade mínima para decolagem v em m/s e o comprimento da pista d em metros, calcule a aceleração constante necessária para que a decolagem seja bem sucedida.

Entrada:
velocidade comprimento

Saída:
aceleracao tempo """

velocidade, comprimento = input().split()
aceleracao = (float(velocidade)*float(velocidade))/(2*float(comprimento))
tempo = (float(velocidade)/aceleracao)
print("%.2f" % aceleracao , "%.2f" % tempo)



