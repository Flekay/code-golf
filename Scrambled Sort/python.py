import sys
for a in sys.argv[1:]:k,*w=a.split();print(*sorted(w,key=lambda x:[*map(k.find,x)]))
