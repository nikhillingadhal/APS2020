def DFS(G,V,i):
	V[i]=True
	for j in range(0,len(G[i])):
		if G[i][j]==1 and V[j]==False:
			print("Nodes visited=",i,j)
			DFS(G,V,j)
edges=int(input())
N=int(input())
G=[]
for i in range(0,N):
	l=[]
	for j in range(0,N):
		l.append(0)	
	G.append(l)
print(G)
for i in range(0,edges):
	node1,node2=map(int,input().split())
	G[node1][node2]=1
	G[node2][node1]=1
V=[]
print(G)
for i in range(0,N):
	V.append(False)
DFS(G,V,0)
