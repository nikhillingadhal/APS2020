val=[3, 9, 14, 15, 20, 25, 26, 31, 37, 42, 43, 48, 53, 54, 59, 65, 70, 71, 76, 81, 82, 87, 93, 98, 99, 105, 110, 111, 116, 121, 122, 127, 133, 138, 139, 144, 149, 150, 155, 161, 166, 167, 172, 177, 178, 183, 189, 194, 195, 200, 201, 206, 207, 212, 217, 218, 223, 229, 234, 235, 240, 245, 246, 251, 257, 262, 263, 268, 273, 274, 279, 285, 290, 291, 296, 302, 303, 308, 313, 314, 319, 325, 330, 331, 336, 341, 342, 347, 353, 358, 359, 364, 369, 370, 375, 381, 386, 387, 392, 397, 398]
T=int(input())
for _ in range(T):
	m1,y1=map(int,input().split())
	m2,y2=map(int,input().split())
	if m1>2:
		y1+=1
	if m2<2:
		y2-=1
	count=0
	val3=y1%400
	val4=y2%400
	count1=0
	if y2-y1>=400:
		count+=((y2-y1)//400)*101
	if val3>val4 and y2>=y1:
		val3,val4=val4,val3
		for i in range(0,len(val)):
			if val[i]>val3 and val[i]<val4:
				count1+=1
		count+=len(val)-count1
	elif y2>=y1:
		for i in range(0,len(val)):
			if val[i]>=val3 and val[i]<=val4:
				count+=1
	print(count)
