def frequencyCount(arr):
  d={} #Dictionary
  for i in range(len(arr)):
    d[i]=arr.count(arr[i])
   return d
A=list(map(int,input().split()))
print(frequencyCount(A))
