import random
a1=input('diga o nome do primeiro aluno: ')
a2=input('diga o nome do segundo: ')
a3=input('diga o nome do terceiro: ')
a4=input('diga o nome do quarto: ')
l=[a1, a2, a3, a4]
print('o nome sorteado foi: ', random.choice(l))