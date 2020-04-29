import math
T=int(input())
l=[0,9,2,3]
for i in range(0,T):
	N=int(input())
	if N==1 :
		print(0)
	elif N==2 or N==3:
		print(1)
	else:
		count=0
		value=2
		newVal=0
		while(N>=newVal):
			count+=1
			newVal=2**(count)
		print(l[(count-1)%4])
