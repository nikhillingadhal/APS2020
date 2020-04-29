T=int(input())
for i in range(0,T):
	N=int(input())
	str1="df"
	str2="jk"
	l=[]
	l1=[]
	finalCount=0
	for j in range(0,N):
		val=input()
		flag1=0
		for w in range(0,len(l)):
			if val==l[w]:
				finalCount+=l1[w]//2
				flag1=1
				break
		if flag1==1:
			continue		
		if val[0] in str1:
			count=2
			flag=1
		elif val[0] in str2:
			flag=-1
			count=2
		for k in range(1,len(val)):
			if val[k] in str1 and flag==-1:
				count+=2
				flag=1
			elif val[k] in str1 and flag==1:
				count+=4
				flag=1
			elif val[k] in str2 and flag==1:
				count+=2
				flag=-1
			elif val[k] in str2 and flag==-1:
				count+=4
				flag=-1
		finalCount+=count
		l.append(val)
		l1.append(count)
	print(finalCount)
