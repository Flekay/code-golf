import sys
r=range(8)
F=lambda p,d,z:p>-1!=(b:=a[p:p+1])>"."and(z,F(p+d,d,1))[b>"O"]
for a in sys.argv[1:]:
 for j in r:print("".join(((c:=a[j*9+i]),"!")[c<"0"and any(F(j*9+i+d,d,0)for d in(~9,~8,~7,~0,1,8,9,10))]for i in r))
 print()