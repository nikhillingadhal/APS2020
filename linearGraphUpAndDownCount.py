N=int(input())
m,c = map(int,input().split())
upCount=0
downCount=0
for _ in range(0,N):
	x,y,p = map(int,input().split())
	val=y-(m*x)-c
	if val>0:
		upCount+=p
	else:
		downCount+=p
print(max(upCount,downCount))
