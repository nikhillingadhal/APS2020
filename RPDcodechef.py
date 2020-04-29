T=int(input())
for _ in range(0,T):
	N=int(input())
	l=[]
	A=list(map(int,input().split()))
	for i in range(0,len(A)):
		for j in range(i+1,len(A)):
			l.append(str(A[i]*A[j]))
	maxVal=0
	for i in range(0,len(l)):
		val=0
		for j in l[i]:
			val+=int(j)
		if val>maxVal:
			maxVal=val
	print(maxVal)
