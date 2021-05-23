'''
Exercício 6 - FOR
Celsius
'''
F = 0

def calculo(F):
  global celsius
  celsius = 5/9*(F-32)


for F in range(50,151,1):
  calculo(F)
  print(F,'graus Fahrenheit equivalem a %.2f ' %celsius,'graus Celsius.\n')