import sys
R=str.replace
Z=print
B=" "
for a in sys.argv[1:]:
 s,c,_,*a=R(a,"\n"," | ").split();s,c=int(s),int(c)
 while~s:exec('''S=""
while a and(j:="|">a[0])*(len(S+a[0])<=c):S+=a.pop(0)+B
if S:
 if(n:=(S:=S[:-1]).count(B))*a*j:d=c-len(S);p=B*(d//n+1);S=R(R(S,B,p),p,p+B,d%n)
 Z(B*s+S)
elif a:Z();a.pop(0)
'''*2);s-=1;c+=2
 Z()
