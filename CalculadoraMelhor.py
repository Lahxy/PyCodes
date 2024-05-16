a=float(input('digite valor de a: '))
b=float(input('digite valor de b: '))
opr=str(input('sinalize a operação: '))
if opr=='+' or opr=='adiçao':
	conta=a+b
if opr=='-' or opr=='subtração':
	conta=a-b
if opr=='*' or opr=='multiplicaçao':
	conta=a*b
if opr=='/' or opr=='divisao':
	conta=a/b
print(f'o resultado da conta entre {a} e {b} eh {conta}')