T=int(input())
for i in range(0,T):
	a=list(map(int,input().split()))
	N=a[0]
	P=a[1]
	a=list(map(int,input().split()))
	a.sort()
	val=0
	for j in range(0,len(a)):
		P-=a[j]
		if P<=0:
			break
		val+=1
	print(val)
