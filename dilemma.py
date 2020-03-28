T=int(input())
for _ in range(T):
	a,b,c,d=map(int,input().split())
	if (c-d)==0 and (b-a)!=0:
		print("NO")
	elif (c-d)==0 and (b-a)==0:
		print("YES")
	elif ((b-a)/abs(c-d)==(b-a)//abs(c-d)):
		print("YES")
	else:
		print("NO")
