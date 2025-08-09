import sys,os
for s in sys.argv[1:]:
 P=i='';a,j=[0]*9**5,0
 for c in s:x="><+-.[".find(c);P+=i+("j+=1","j-=1","a[j]+=1","a[j]-=1","os.write(1,bytes([a[j]&255]))","while a[j]:","")[x]+"\n";i=i[c==']':]+' '[c!='[':]
 exec(P)
