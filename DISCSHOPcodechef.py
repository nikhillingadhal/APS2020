T=int(input())
for _ in range(0,T):
	val=input()
	val=list(val)
	l=val[:]
	minVal=10000000000
	for i in range(0,len(val)):
		l.pop(i)
		value=int(''.join(l))
		if value<minVal:
			minVal=value
		l=val[:]
	print(minVal)
