T=int(input())
for T in range(0,T):
	s=input()
	s1=input()
	count=0
	for i in s1:
		if i in s:
			count+=1
	print(count)
