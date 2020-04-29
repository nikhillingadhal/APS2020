T=int(input())
for _ in range(0,T):
	N=int(input())
	S=input()
	d={}
	l1=[]
	if(len(S)==1):
		print(0)
		continue
	for i in range(0,len(S)):
		d[S[i]]=[]
	for i in range(0,len(S)):
		d[S[i]].append(i)
	l=list(d.keys())
	for i in range(0,len(l)):
		minVal=10000
		flag=0
		for j in range(0,len(d[l[i]])-1):
			if d[l[i]][j+1]-d[l[i]][j] < minVal:
				minVal=d[l[i]][j+1]-d[l[i]][j]
			flag=1
		if(flag==1):
			l1.append(len(S)-minVal)
	if(len(l1)!=0):
		print(max(l1))
	else:
		print(0)
