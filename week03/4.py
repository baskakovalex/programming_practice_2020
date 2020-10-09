a = [int(s) for s in input().split()]
b=[]
b.append(a[0])
fault=1
for i in range(0,len(a)) :
  for j in range (len(b)):
    if a[i]==b[j]:
      fault=1
  if fault==0:
    b.append(a[i])
  fault=0
print (b)
