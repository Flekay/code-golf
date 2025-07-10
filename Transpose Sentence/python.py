import sys
for a in sys.argv[1:]:
 s=a.split();o=''
 for i in range(len(max(s,key=len))):
  for x in s:o+=''if len(x)-1<i else x[i]
  o+=' '
 print(o)
