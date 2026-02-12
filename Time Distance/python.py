import sys
l=1,60,60,24,7,30/7,12;u="second minute hour day week month".split()
for a in sys.argv[1:]:
 a=int(a);A=abs(a);t=""
 for i in range(6):
  A/=l[i]
  if A<l[i+1]:A=int(A);t+=f"{A} {u[i]}s"*(A>1)or f"a{'n'*(i==2)} {u[i]}";break
 else:A=int(abs(a)/31536e3);t+=f"{A} years"*(A>1)or'a year'
 print(("in "+t,t+" ago")[a<0]if a else"now")
