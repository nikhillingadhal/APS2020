import math
T=int(input())
for i in range(0,T):
	N=int(input())
	P=list(map(int,input().split()))
	val=[math.inf,math.inf,math.inf,math.inf,math.inf]
	good=0
	k=0
	for j in range(0,len(P)):
		minVal=P[j]
		flag=0
		for k in range(0,len(val)):
			if val[k]<=minVal:
				flag=1
				break
		if flag==0:
			good+=1
		val.pop(0)
		val.append(P[j])
	print(good)
