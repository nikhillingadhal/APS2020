import math
T=int(input())
for i in range(0,T):
	N=int(input())
	count=0
	while N!=0:
		N=N//5
		count+=N
	print(count)
