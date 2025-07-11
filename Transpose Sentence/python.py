import sys
for a in sys.argv[1:]:s=a.split();print(*[''.join(x[i:i+1]for x in s)for i in range(len(max(s,key=len)))])
