T=int(input())
for i in range(T):
	a=list(map(int,input().split()))
	N=a[0]
	m=a[1]
	k=a[2]
	l=[]
	xaxis=[]
	d={}
	count=0
	for j in range(k):
		b=list(map(int,input().split()))
		x=(b[0])
		y=(b[1])
		l.append([x,y])
	for k in range(len(l)):
		d[k[0]]=k[1]
	print(d)
	keys=d.keys()
	values=d.values()
	for val in l:
		x1=val[0]
		y1=val[1]
		if y1+1 not in d[x1]:
			count+=1
		if y1-1 not in d[x1]:
			count+=1
		if x1+1 not in keys:
			count+=1
		elif y1 not in d[x1+1]:
			count+=1
		if x1-1 not in keys:
			count+=1
		elif y1 not in d[x1-1]:
			count+=1
	print(count)
