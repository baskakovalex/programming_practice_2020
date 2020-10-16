def nod(a,b):
  while a != 0 and b != 0:
    if a >=b:
      a=a % b
    else:
      b=b%a
  return b+a
print (nod(a=int(input()),b=int(input())))
