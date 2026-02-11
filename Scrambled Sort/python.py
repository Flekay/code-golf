import sys
for a in sys.argv[1:]:
 w=a.split()
 k=w[0]
 print(*sorted(w[1:],key=lambda x:[k.index(c)for c in x]))
