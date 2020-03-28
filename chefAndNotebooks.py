T=int(input())
for _ in range(T):
	X,Y,K,N = map(int,input().split())
	val=X-Y
	l=[]
	for i in range(0,N):
		a=list(map(int,input().split()))
		l.append(a)
	flag=0
	for i in range(0,len(l)):
		if l[i][0] >= val and l[i][1] <= K:
			flag=1
	if flag==1:
		print("LuckyChef")
	else:
		print("UnluckyChef")
