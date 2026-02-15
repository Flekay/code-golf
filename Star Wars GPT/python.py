import sys,re
for a in sys.argv[1:]:
 t,*P=a.split('\n')
 for p in P:print(max(s:=re.findall(rf'\b{p} (\S+)',t),key=s.count))
