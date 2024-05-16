import random
a=input('diga o primeiro: ')
b=input('diga o segundo: ')
c=input('diga o terceiro: ')
list=[a, b, c]
random.shuffle(list)
print(list)