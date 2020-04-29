T=int(input())
for T in range(0,T):
	s=input()
	if "010" in s or "101" in s:
		print("Good")
	else:
		print("Bad")
