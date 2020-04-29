T=int(input())
for _ in range(0,T):
	n,m=map(int,input().split())
	A=list(map(int,input().split()))
	B=list(range(1,n+1))
	A=set(A)
	B=set(B)
	C=B.difference(A)
	C=list(C)
	C.sort()
	for i in range(0,len(C)):
		if i%2==0:
			print(C[i],end=' ')
	print()
	for i in range(0,len(C)):
		if i%2==1:
			print(C[i],end=' ')
	print()
