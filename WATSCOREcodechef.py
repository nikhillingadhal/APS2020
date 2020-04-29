T=int(input())
for _ in range(0,T):
	N=int(input())
	d={}
	for i in range(0,N):
		A=list(map(int,input().split()))
		i=A[0]
		S=A[1]
		if i>8:
			continue
		elif i not in list(d.keys()):
			d[i]=S
		elif d[i] < S:
			d[i]=S
	print(sum(list(d.values())))
