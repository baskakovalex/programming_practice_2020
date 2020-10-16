def power(a,n):
  b=1
  for i in range(abs(n)):
    b*=a
  if n>0:
    return b
  elif n==0:
    return 1
  else:
    return 1/b
a=float(input())
n=int(input())
print (power(a,n))
