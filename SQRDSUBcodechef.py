T=int(input()) 
for _ in range(T):
	N=int(input())
	A=list(map(int,input().split()))
	count=0
	A4=[]
	A2=[]
	for i in range(N):
		if(A[i]%4==0):
			A[i]=4
			A4.append(i)
		if(A[i]%2==0):
			A[i]=2
			A2.append(i)
	i4=0
	i2=0
	count=0
	i4Len=len(A4)
	i2Len=len(A2)
	for i in range(N):
		if i2<i2Len:
				if i>A2[i2]:
					i2+=1
		if i4<i4Len:
			if i>A4[i4]:
				i4+=1
		if A[i]%2!=0:
			count+=1
			if i2<i2Len:
				val=len(A2[i2:])
			else:
				val=0
			if val==0:
				count+=N-(i+1)
			elif val==1:
				k=A2[i2]-i-1
				j=0
				if i4<i4Len:
					j=A4[i4]
					count+=N-j
					count+=min(j-i-1,k)
				else:
					ty=1
					count+=k
			else:
				j=A2[i2]-i-1
				k=j
				j=A2[i2+1]
				if i4<i4Len:
					val1=A4[i4]
				else:
					val1=N+1
				j=min(j,val1)
				count+=N-(j+1)+1
				count+=min(val1-i-1,k)
		else:
			if(A[i]%4==0):
				count+=N-i
			else:
				if i2+1<i2Len:
					j=A2[i2+1]
				else:
					j=N
				if i4<i4Len:
					val2=A4[i4]
				else:
					val2=N+1
				j=min(j,val2)
				count+=N-(j+1)+1
	print(count)
