#perguntas sobre o imposto de renda
tem_ir=input('CALCULAR COM IMPOSTO DE RENDA? sim ou não: ')
if tem_ir=='sim':
	ir=1-((float(input('ATUALIZE-ME SOBRE A ALÍQUOTA DO IMPOSTO DE RENDA: ')))/100)
	valor_a_deduzir=float(input('ATUALIZE-ME SOBRE O VALOR A DEDUZIR DO IR, CASO HAJA: '))
else:
	ir=0
	valor_a_deduzir=0
print('\n')
#determinando um valor qualquer pra algumas variáveis pra não dar erro
end='sim'
rpt_total=1
#ciclo da calculadora
while end=='sim':
	valor_inicial=float(input('VALOR INICIAL: '))
	taxa=float(input('TAXA MENSAL: '))
	valor_mensal=float(input('INVESTIMENTO MENSAL: '))
	tempo=float(input('TEMPO EM MESES: '))
	rpt=0
	m=valor_inicial
	print(f'\nINICIAL - {m:.2f}\n')
#primeiros meses
	while rpt != tempo:
		rpt=rpt+1
		m=(m*(1+taxa/100))+valor_mensal
		if rpt != tempo: 
			print (f'{rpt}° mês - {m:.2f}')
#último mês
	else:
		if rpt_total==1:
			valor_investido=(valor_inicial+(valor_mensal*tempo))
			valor_investido_geral=valor_investido
			valor_ganho_investimento=m-valor_investido
			valor_ganho_investimento_geral=valor_ganho_investimento		
		else:
			valor_investido=valor_mensal*tempo
			valor_investido_geral=valor_investido+valor_investido_geral
			valor_ganho_investimento=m-valor_investido-valor_inicial
			valor_ganho_investimento_geral=valor_ganho_investimento+valor_ganho_investimento_geral		
		valor_final_ir=(m*ir)+valor_a_deduzir
#resultados		
		print(f'\nFINAL: {rpt}° mês - {m:.2f}\n')
		print(f'VALOR INVESTIDO: {valor_investido:.2f}')
		print (f'VALOR GANHO PELO INVESTIMENTO: {valor_ganho_investimento:.2f}')
		print(f'\nVALOR INVESTIDO GERAL: {valor_investido_geral:.2f}')
		print(f'VALOR GANHO PELO INVESTIMENTO GERAL: {valor_ganho_investimento_geral:.2f}')
		print (f'VALOR FINAL COM IR: {valor_final_ir:.2f}')
		end=input('\n\nDIGA SE VOCÊ PRETENDE CONTINUAR, sim ou não: ')
		rpt_total+=1
		print('\n')