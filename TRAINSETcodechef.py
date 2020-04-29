t=int(input())
for q in range(t):
	n=int(input())
	d={}
	k=[]
	l=[]
	for i in range(n):
		s,v=input().split(" ")
		k.append(v)
		l.append(s)
		d[s]=[]
	for i in range(n):
		d[l[i]].append(k[i])
	val=list(d.values())
	val1=list(d.keys())
	count=0
	for j in range(len(val1)):
		s="".join(val[j])
		c=s.count('0')
		c1=s.count('1')
		if(c>c1):
			count+=c
		else:
			count+=c1
	print(count)
