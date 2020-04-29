T=int(input())
for _ in range(0,T):
	N=int(input())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))
	A.sort()
	B.sort()
	l=[]
	for i in range(0,N):
		l.append(min(A[i],B[i]))
	print(sum(l))
