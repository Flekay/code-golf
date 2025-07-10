import sys
m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for r in sys.argv[1:]:
 n=0
 for i in range(len(r)):n+=m[r[i]]*(1if i==len(r)-1or m[r[i]]>=m[r[i+1]]else-1)
 print(n)
