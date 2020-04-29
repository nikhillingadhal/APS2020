T=int(input())
for i in range(0,T):
	N=int(input())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))
	l=[]
	for j in range(0,N):
		val=(A[j]*20)-(B[j]*10)
		if val>0:
			l.append(val)
		else:
			l.append(0)
	print(max(l))
