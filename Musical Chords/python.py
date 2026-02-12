import sys
for a in sys.argv[1:]:
 N=a.split();R=0,1,2;L=[ord(n[0])-65for n in N];P=[((l:=L[j])*2-(l>1)-(l>4)+("♯"in N[j])-("♭"in N[j]))%12for j in R];i=next(j for j in R if(L[j]+2)%7in L if(L[j]+4)%7in L);r=P[i];print(N[i]+["°","m","","+"][sum((x-r)%12for x in P)-9])
