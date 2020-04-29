import math
T=int(input())
for i in range(0,T):
	A=list(map(int,input().split()))
	N=A[0]
	K=A[1]
	A=list(map(int,input().split()))
	A.sort()
	d1={}
	d={}
	B=A[:K]
	C=set(B)
	C=list(C)
	for j in range(0,K):
		d1[A[j]]=0
		d[A[j]]=0
	for j in range(0,len(C)):
		for k in range(0,len(A)):
			if A[k]==C[j]:
				d1[C[j]]+=1
	for j in range(0,len(C)):
		for k in range(0,len(B)):
			if B[k]==C[j]:
				d[C[j]]+=1
	val=list(d.values())
	val1=list(d1.values())
	newVal=1
	for j in range(0,len(val)):
		newVal=newVal*(math.factorial(val1[j])//(math.factorial(val1[j]-val[j])*math.factorial(val[j])))
	print(newVal)
