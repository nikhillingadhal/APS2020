val=input()
a=[]
for i in val:
	if i!=' ':
		var=ord(i)
		var1=bin(var)
		a.append(var1[2:])
	else:
		a.append('0000000')
for i in range(0,len(a)):
	print(a[i],end=' ')
