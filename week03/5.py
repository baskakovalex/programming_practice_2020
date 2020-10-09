a = [int(s) for s in input().split()]
b=[int(s) for s in input().split()]
c=set(a)&set(b)
sorted(c)
print(c)
