T=int(input())
for _ in range(T):
	N,K=map(int,input().split())
	A=list(map(int,input().split()))
	l=[]
	for i in range(len(A)):
		l.append(A[i]%K)
	val=sum(l)
	result=val%K
	print(result)
