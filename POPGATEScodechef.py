T=int(input())
for _ in range(T):
	N,K=map(int,input().split())
	L=list(map(str,input().split()))
	for i in range(0,K):
		A=L.pop()
		if A=='H':
			for j in range(0,len(L)):
				if L[j]=='H':
					L[j]='T'
				else:
					L[j]='H'
	val=''.join(L)
	print(val.count('H'))
