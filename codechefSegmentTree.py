import math
import sys
sys.setrecursionlimit(10000000)
def createTree(a,stree,low,high,pos):
	if low==high:
		stree[pos]=a[low]
		return
	mid=(low+high)//2
	createTree(a,stree,low,mid,(2*pos)+1)
	createTree(a,stree,mid+1,high,(2*pos)+2)
	stree[pos]=min(stree[(2*pos)+1],stree[(2*pos)+2])
def minQuery(stree,qlow,qhigh,low,high,pos):
	if qlow<=low and qhigh>=high:
		return stree[pos]
	if qlow>high or qhigh<low:
		return sys.maxsize
	mid=low+(high-low)//2
	return min(minQuery(stree,qlow,qhigh,low,mid,(2*pos)+1),minQuery(stree,qlow,qhigh,mid+1,high,(2*pos)+2))

N,Q=map(int,input().split())
A=list(map(int,input().split()))
n=len(A)
val=int(math.ceil(math.log2(n)))
val1=2*(2**val)-1
stree=[sys.maxsize]*val1
createTree(A,stree,0,n-1,0)
for _ in range(Q):
	stree=[sys.maxsize]*val1
	createTree(A,stree,0,n-1,0)
	print(A)
	B=list(map(int,input().split()))
	if B[0]==0:
		print(minQuery(stree,B[1],B[2],0,n-1,0))
	if B[0]==1:
		for i in range(B[1]-1,B[2]):
			A[i]=(A[i]&B[3])
