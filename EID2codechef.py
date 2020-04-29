T=int(input())
for i in range(0,T):
	A=list(map(int,input().split()))
	A1=A[:3]
	C1=A[3:]
	val1 = A1.index(max(A1))
	val2 = C1.index(max(C1))
	if val1 == val2:
		test = max(A1)
		testc = max(C1)
		A1.remove(test)
		C1.remove(testc)
		val3 = A1.index(max(A1))
		val4 = C1.index(max(C1))
		if ((test == max(A1) and testc != max(C1)) or (test != max(A1) and testc == max(C1))):
			print("NOT FAIR")
		else:
			test1 = max(A1)
			testc1 = max(C1)
			if val3 == val4:
				A1.remove(test1)
				C1.remove(testc1)
				if (test1==A1[0] and testc1 !=C1[0]) or (test1!=A1[0] and testc1 ==C1[0]):
					print("NOT FAIR")
				else:
					print("FAIR")
			else:
				print("NOT FAIR")
	else:
		print("NOT FAIR")
