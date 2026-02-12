import sys
for a in sys.argv[1:]:
 A=abs(a:=int(a));i=0;D=1
 for m in 60,60,24,7,30/7,12:
  if A<D*m:break
  D*=m;i+=1
 v=int(A/[D,31536e3][i>5]);n="second minute hour day week month year".split()[i];t=f"{v} {n}s"*(v>1)or"a"+"n"*(i==2)+" "+n;print(a and("in "+t,t+" ago")[a<0]or"now")
