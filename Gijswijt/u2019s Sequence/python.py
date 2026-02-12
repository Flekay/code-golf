s="1"
while(l:=len(s))<1000:s+=str(max(j*(s[-i:]*j==s[-i*j:])for i in range(l)for j in range(5)))
*map(print,s),
