from itertools import combinations
T=int(input())
for _ in range(0,T):
	n,m=map(int,input().split())
	l=[]
	per=[]
	for i in range(0,n):
		l.append(int(input()))
	for i in range(1,len(l)+1):
		per.append(list(combinations(l,i)))
	l=list(per)
	flag=0
	for i in range(0,len(l)):
		for k in range(0,len(l[i])):
			try:
				if sum(l[i][k])==m:
					flag=1
					print("Yes")
					break
			except:
				continue
		if flag==1:
			break
	if flag==0:
		print("No")
