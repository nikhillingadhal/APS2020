import math
T=int(input())
for i in range(0,T):
	N=int(input())
	A=int(input())
	S=(((10**N)-1)*2)+2+A
	print(S,flush=True)
	B=int(input())
	C=S-(A+B+(10**N))
	print(C,flush=True)
	D=int(input())
	E=S-(A+B+C+D)
	print(E,flush=True)
	val=int(input())
