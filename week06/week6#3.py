def sur(r):
  return 3.14*r**2
def rec(a,b):
  return a*b
def tri(h,a):
  return (h*a)/2
q=int(input ("chose figure \n1)surcle  \n2) rectangle \n3)triangle \n"))
if q==1:
  print (sur(r=float(input("input radius "))))
elif q==2:
  print (rec(a=float(input("input a side ")),b=float(input("input b side "))))
elif q==3:
  print (tri(h=float(input("input height ")),a=float(input("input side "))))
