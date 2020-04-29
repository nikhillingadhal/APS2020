T=int(input())
for _ in range(0,T):
	A=list(map(int,input().split()))
	N=A[0]
	K=A[1]
	A=list(map(int,input().split()))
	val=0
	flag=0
	for i in range(0,len(A)):
		if A[i]>=K:
			val+=A[i]-K
		elif A[i]<K:
			if (val+A[i])>=K:
				val=(val+A[i])-K
			elif (val+A[i])<K:
				flag=1
				break
	if flag==0:
		print("YES")
	else:
		print("NO",i+1)
