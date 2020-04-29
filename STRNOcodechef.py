import math as mt 
def isPrime(n) : 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	if (n % 2 == 0 or n % 3 == 0) : 
		return False
	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
	return True
def kFactors(n, k): 
	a = list() 
	while n % 2 == 0: 
		a.append(2) 
		n = n // 2
	for i in range(3, mt.ceil(mt.sqrt(n)), 2): 
		while n % i == 0: 
			n = n / i; 
			a.append(i) 
	if n > 2: 
		a.append(n) 
	if len(a) < k: 
		print(0) 
		return
	else:
		print(1)
		return
T=int(input())
for _ in range(T):
	X,K=map(int,input().split())
	if K==1:
		if X>1:
			print(1)
		else:
			print(0)
	if K==2:
		if X>2:
			if isPrime(X):
				print(0)
			else:
				print(1)
		else:
			print(0)
	if K>2:
		if X<3:
			print(0)
		else:
			kFactors(X,K)
