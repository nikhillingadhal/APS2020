T=int(input())
for i in range(0,T):
	A=list(map(int,input().split()))
	N=A[0]
	K=A[1]
	if (N//K)%K==0:
		print("NO")
	else:
		print("YES")	
