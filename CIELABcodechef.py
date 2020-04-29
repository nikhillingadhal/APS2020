L=list(map(int,input().split()))
A=L[0]
B=L[1]
C=A-B
D=str(C)
N=str(C)
D=list(D)
S="123456789"
for i in S:
	if D[0]!=i:
		D[0]=i
		break
print(int(''.join(D)))
