nome=input('me informe o seu nome: ')
sexo=str(input('me diga seu sexo, digite 1 para masculino e 2 para feminino: '))
idade=int(input('me diga sua idade: '))
if idade < 30:
	tratamento='você'
if sexo=='1' and idade>=30:
	tratamento='o senhor'
if sexo=='2' and idade>=30:
	tratamento='a senhora'
peso=int(input(tratamento+' pesa: '))
print('confira as informações a seguir: \n')
print('nome: ',nome)
if sexo=='1':
	sexo='masculino'
if sexo=='2':
	sexo='feminino'
print('sexo: ',sexo)
print('idade: ',idade)
print('peso: ',peso,'quilos')