import sys;M=60,60,24,7,30/7,73/6,9e9
for a in sys.argv[1:]:
 A=abs(a:=int(a));D=1;i=0
 while A>=D*M[i]:D*=M[i];i+=1
 v=int(A/D);n="second minute hour day week month year".split()[i];t=f"{v} {n}s"*(v>1)or"a"+"n "[i!=2:]+n;print(a and("in "+t,t+" ago")[a<0]or"now")