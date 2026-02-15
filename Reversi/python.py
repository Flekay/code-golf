import sys
F=lambda p,d,z:p>-1!=(b:=a[p:p+1])>"."and(z,F(p+d,d,1))[b>"O"]
for a in sys.argv[1:]:print("".join((c,"!")[any(F(p+d,d,0)for d in(~9,~8,~7,~0,1,8,9,10)if"."==c)]for p,c in enumerate(a))+"\n")