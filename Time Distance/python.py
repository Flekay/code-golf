import sys
l=1,60,60,24,7,30/7,12;u="second minute hour day week month".split()
for a in sys.argv[1:]:
 a=int(a);A=abs(a)
 for i in range(6):
  if(A:=A/l[i])<l[i+1]:A=int(A);t=f"{A} {u[i]}s"*(A>1)or f"a{'n'*(i==2)} {u[i]}";break
 else:A=int(abs(a)/31536e3);t=f"{A} years"*(A>1)or'a year'
 print(a and("in "+t,t+" ago")[a<0]or"now")
