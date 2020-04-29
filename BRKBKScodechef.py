T=int(input())
for _ in range(0,T):
	A=list(map(int,input().split()))
	S=A[0]
	W=[]
	for i in range(1,len(A)):
		W.append(A[i])
	count=0
	if W[0]+W[1]+W[2]<=S:
		count+=1
	elif W[0]+W[1]<=S or W[1]+W[2]<=S:
		count+=2
	elif W[0]<=S:
		count+=3
	print(count)
