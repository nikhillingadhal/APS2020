T=int(input())
for i in range(0,T):
	A=list(map(int,input().split()))
	N=A[0]
	M=A[1]
	S=A[2]
	A=list(map(int,input().split()))
	A.sort()
	count=0
	for i in range(0,len(A)):
		if A[i]<=S and M>0:
			count+=1
			M-=1
		elif A[i]<=(S*2) and M>1:
			count+=1
			M-=2
	print(count)
