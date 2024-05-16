import random
simbologia='1234567890qwertyuiopasdfghjklzxcvbnm%^~êèěęėëéř|þț[ťý]ùûů<űüúìîı>ïíºóôõöøō{ò}@ąăåäãâáàªß#șšşśð&ď*ğ-+=()ź_žż£¢$¥€çč"ć:ñň;ń/!,.?'*100
simbologia=simbologia+simbologia.upper()
while 2==2:
	rst=''.join(random.sample(simbologia,9999))
	print(rst)