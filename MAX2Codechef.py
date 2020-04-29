N=int(input())
A=input()
A=list(A)
count=0
maxCount=0
for i in range(0,len(A)):
	if A[i]=='1':
		count+=1
		newVal=i
		if(count==2):
			maxCount=i
			break
if(maxCount==0):
	maxCount=len(A)-newVal-1
print(maxCount)
