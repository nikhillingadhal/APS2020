T=int(input())
for _ in range(0,T):
	n,m=map(int,input().split())
	M=[]
	for i in range(0,n):
		A=list(map(int,input().split()))
		M.append(A)
	count=0
	for j in range(1,n):
		for k in range(0,m):
			val=1
			while(1):
				try:
					if k-val<0 or j-val<0:
						break
					if M[j][k+val] == M[j][k-val] and M[j+val][k] == M[j-val][k]:
						count+=1
						val+=1
					else:
						break
				except:
					break
	print(count+(m*n))
