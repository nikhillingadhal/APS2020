def BFS(G,V,i):
	stack=[]
	stack.append(i)
	while(len(stack)!=0):
		i=stack.pop()
		V[i]=True
		for j in range(0,len(G[i])):
			if G[i][j]==1 and V[j]==False:
				V[j]=True
				print("Visited Vertices=",i,j)
				stack.append(j)
edges=int(input())
N=int(input())
G=[]
for i in range(0,N):
	l=[]
	for j in range(0,N):
		l.append(0)	
	G.append(l)
for i in range(0,edges):
	node1,node2=map(int,input().split())
	G[node1][node2]=1
	G[node2][node1]=1
V=[]
for i in range(0,N):
	V.append(False)
BFS(G,V,0)
