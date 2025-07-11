import sys
R=str.replace
Z=print
B=" "
for a in sys.argv[1:]:
	P=lambda:a.pop(0);a=R(a,"\n"," | ").split(B);s=int(P());c=int(P());P()
	for i in range((s+1)*2):
		S=""
		while a and a[0]!="|"and len(S+a[0])<=c:S+=P()+B
		if S:
			S=S[:-1]
			if B in S and a and a[0]!="|":D,M=divmod(c-len(S),S.count(B));p=B*(D+1);S=R(R(S,B,p),p,p+B,M)
			Z(B*s+S)
		elif a:Z();P()
		if i%2:s-=1;c+=2
	Z()
