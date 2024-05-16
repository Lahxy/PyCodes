n=1
p=1
while True:	
	n2=int(n/2)
	cont = 0
	for i in range(1, n2+1):
		if n%i == 0:
			cont += 1
	if cont == 1 and n!=1:
		print (n,"   ",p,"°")
		p+=1
	n+=1