T=int(input())
for _ in range(T):
	N,P=map(int,input().split())
	A=list(map(int,input().split()))
	d={}
	flag1=0
	for i in range(0,len(A)):
		d[A[i]]=0
	flag=0
	for i in range(0,len(A)):
		if P%A[i]!=0:
			d[A[i]]=P//A[i]+1
			flag=1
			break
	if flag==1:
		print("YES",end=" ")
		for i in range(0,len(A)):
			print(d[A[i]],end=" ")
		print()
		flag1=1
	else:
		flag2=0
		for i in range(0,len(A)-1):
			if A[i+1]%A[i]!=0:
				val=A[i+1]
				val1=A[i]
				flag2=1
				break
		if flag2==1:
			var=P//val
			var-=1
			var1=val//val1
			var1+=1
			d[val]=var
			d[val1]=var1
			print("YES",end=" ")
			for i in range(0,len(A)):
				print(d[A[i]],end=" ")
			print()
			flag1=1
	if flag1!=1:
		print("NO")
