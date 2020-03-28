while(1):
	N=int(input())
	val=1
	for i in range(1,N):
		val = (val*((4*i)+2))//(i+2)
	print(val)
