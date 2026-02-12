import sys
for s in sys.argv[1:]:
 P=i='';a,j=[0]*9**5,0
 for c in s:P+=i+"while a[j]:||||a[j]+=1||a[j]-=1|print(end=chr(a[j]%256))|j-=1||j+=1".split("|")[ord(c)%13]+"\n";i=i[c>'[':]+' '[c!='[':]
 exec(P)
