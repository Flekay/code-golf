import sys
for a in sys.argv[1:]:
 N=a.split();R=0,1,2;L=[ord(n[0])%7for n in N];P=[((l:=L[j])*2+9-(l>3)+("♯"in N[j])*2-len(N[j]))%12for j in R];i=next(j for j in R if{(L[j]+2)%7,(L[j]+4)%7}<={*L});print(N[i]+["°","m","","+"][sum((x-P[i])%12for x in P)-9])
