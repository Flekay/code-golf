import sys
for a in sys.argv[1:]:N,L,P=zip(*[(n,l:=ord(n[0])%7,l*2+9-l//4+("♯"in n)*2-len(n))for n in a.split()]);print(N[i:=L.index(~sum(L)*2%7)]+"+°m "[(sum(P)+P[i])%4].strip())