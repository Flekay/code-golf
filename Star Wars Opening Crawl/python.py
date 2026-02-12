import sys
R=str.replace
Z=print
B=" "
def F(S=""):
 while a and a[0]<"|"and len(S+a[0])<=c:S+=a.pop(0)+B
 if S:
  if(n:=(S:=S[:-1]).count(B))and a and a[0]<"|":d=c-len(S);p=B*(d//n+1);S=R(R(S,B,p),p,p+B,d%n)
  Z(B*s+S)
 elif a:Z();a.pop(0)
for a in sys.argv[1:]:
 a=R(a,"\n"," | ").split(B);s,c=map(int,a[:2]);a=a[3:]
 while-~s:F();F();s-=1;c+=2
 Z()
