import sys
for l in sys.argv[1:]:
 l=l.split();d=g=p=0;m=[0]*3
 for x in l:
  if g!=x:p+=m[p]
  if p>2:break
  d|=l.index(x)<1and l.count(x)<2
  m[p]+=1;g=x
 print(f"{'1💎 '*d}{m[0]}🥇{f' {m[1]}🥈'*(m[1]>0)}{f' {m[2]}🥉'*(m[2]>0)}")
