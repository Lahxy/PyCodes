x=input('diga seu nome completo: ')
print(f'seu nome todo maiúsculo fica: {x.upper()}')
print(f'seu nome todo minúsculo fica: {x.lower()}')
x2=x.replace(' ','')
print(f'o número de letras em seu nome é: {len(x2)}')
prim_nome=x.split()[0]
print(f'o seu primeiro nome, {prim_nome}, tem {len(prim_nome)} letras')