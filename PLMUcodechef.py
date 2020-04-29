import math
T=int(input())
for _ in range(0,T):
	N=int(input())
	A=list(map(int,input().split()))
	count=0
	count0=0
	for i in range(0,len(A)):	
		if A[i]==2:
			count+=1
		if A[i]==0:
			count0+=1
	var=count
	var1=count0
	if var>2:
		ans=(math.factorial(var))//(math.factorial(var-2)*2)
	elif var==2:
		ans=1
	else:
		ans=0
	if var1>2:
		ans1=(math.factorial(var1))//(math.factorial(var1-2)*2)
	elif var1==2:
		ans1=1
	else:
		ans1=0	
	print(ans+ans1)
