def fun(val,P,Q):
	if val==1 and (P!=val or Q!=val):
		print(1,1)
		 
	if val==2:
		if (P+Q)//2==val:
			if P!=1 and Q!=3:
				print(1,3)
			if P!=3 and Q!=1:
				print(3,1)
			print(2,2)
			 
		else:
			print(2,2)
			print(1,3)
			print(3,1)
			print(2,2)
			 
	if val==3:
		if (P+Q)//2==val:
			if P!=1 and Q!=5:
				print(1,5)
			if P!=5 and Q!=1: 
				print(5,1)
			print(3,3)
			 
		else:
			print(3,3)
			print(1,5)
			print(5,1)
			print(3,3)
			 
	if val==4:
		if (P+Q)//2==val:
			if P!=1 and Q!=7:
				print(1,7)
			if P!=7 and Q!=1:
				print(7,1)
			print(4,4)
			 
		else:
			print(4,4)
			print(1,7)
			print(7,1)
			print(4,4)
			 
			
	if val==5:
		if (P+Q)//2==val:
			if P!=8 and Q!=2:
				print(8,2)
			if P!=2 and Q!=8:
				print(2,8)
			print(5,5)
			 
			
		else:
			print(5,5)
			print(8,2)
			print(2,8)
			print(5,5)
			 
	
	if val==6:
		if (P+Q)//2==val:
			if P!=8 and Q!=4:
				print(8,4)
			if P!=4 and Q!=8:
				print(4,8)
			print(6,6)
			 
		else:
			print(6,6)
			print(8,4)
			print(4,8)
			print(6,6)
			 
			
	if val==7:
		if (P+Q)//2==val:
			if P!=6 and Q!=8:
				print(6,8)
			if P!=8 and Q!=6:
				print(8,6)
			print(7,7)
			 
	
		else:
			print(7,7)
			print(6,8)
			print(8,6)
			print(7,7)
			 
	if val==8 and (P!=val or Q!=val):
		print(8,8)
		 
def countBox(val,P,Q):
	count=0
	if val==1 and (P!=val or Q!=val):
		count+=1
		 
	if val==2:
		if (P+Q)//2==val:
			if P!=1 and Q!=3:
				count+=1
			if P!=3 and Q!=1:
				count+=1
			count+=1
			 
		else:
			count+=1
			count+=1
			count+=1
			count+=1
			 
	if val==3:
		if (P+Q)//2==val:
			if P!=1 and Q!=5:
				count+=1
			if P!=5 and Q!=1: 
				count+=1
			count+=1
			 
		else:
			count+=1
			count+=1
			count+=1
			count+=1
			 
	if val==4:
		if (P+Q)//2==val:
			if P!=1 and Q!=7:
				count+=1
			if P!=7 and Q!=1:
				count+=1
			count+=1
			 
		else:
			count+=1
			count+=1
			count+=1
			count+=1
			 
			
	if val==5:
		if (P+Q)//2==val:
			if P!=8 and Q!=2:
				count+=1
			if P!=2 and Q!=8:
				count+=1
			count+=1
			 
			
		else:
			count+=1
			count+=1
			count+=1
			count+=1
			 
	
	if val==6:
		if (P+Q)//2==val:
			if P!=8 and Q!=4:
				count+=1
			if P!=4 and Q!=8:
				count+=1
			count+=1
			 
		else:
			count+=1
			count+=1
			count+=1
			count+=1
			 
			
	if val==7:
		if (P+Q)//2==val:
			if P!=6 and Q!=8:
				count+=1
			if P!=8 and Q!=6:
				count+=1
			count+=1
			 
	
		else:
			count+=1
			count+=1
			count+=1
			count+=1
			 
	if val==8 and (P!=val or Q!=val):
		count+=1
	return count
	
T=int(input())
for _ in range(0,T):
	P,Q=map(int,input().split())
	val=(P+Q)//2
	val1=(P+Q)//2
	count=0
	while(val!=9):
		count+=countBox(val,P,Q)
		val+=1
	while(val1!=1):
		val1-=1
		count+=countBox(val1,P,Q)
	print(count)
	val=(P+Q)//2
	val1=(P+Q)//2
	while(val!=9):
		fun(val,P,Q)
		val+=1
	while(val1!=1):
		val1-=1
		fun(val1,P,Q)
