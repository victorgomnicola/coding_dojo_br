a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangle = a*c/2
circle = 3.14159*c*c
trapezium = (a+b)*c/2
square = b*b
rectangle = a*b

print('TRIANGULO:', '{0:.3f}'.format(triangle))
print('CIRCULO:', '{0:.3f}'.format(circle))
print('TRAPEZIO:', '{0:.3f}'.format(trapezium))
print('QUADRADO:', '{0:.3f}'.format(square))
print('RETANGULO:', '{0:.3f}'.format(rectangle))