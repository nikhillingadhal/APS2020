import sys
T=int(input())
for _ in range(0,T):
	N,M=map(int,input().split())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))
	l={}
	for i in range(0,len(A)):
		l[A[i]]=0
	for i in range(0,len(A)):
		l[A[i]]+=B[i]
	l1=list(l.values())
	print(min(l1))
