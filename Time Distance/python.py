import sys;M=60,60,24,7,30/7,73/6,9e9
for a in sys.argv[1:]:
 A=abs(a:=int(a));i=0
 while A>=M[i]:A/=M[i];i+=1
 t=("%d %ss"%(A,n:="second minute hour day week month year".split()[i]),"a"+"n "[i!=2:]+n)[A<2];print(a and("in "+t,t+" ago")[a<0]or"now")