m,M=min,max
for i in[(lambda z:(r:=set(),q:=[[(0,0)]],[(q.append(c+[(x+a,y+b)])if len(c)<z and(x+a,y+b)not in c else 0)or(r.add((*sorted((x-min(x for x,y in c),y-min(y for x,y in c))for x,y in c),))if len(c)==z else 0)for c in q for x,y in c for a,b in[(0,1),(1,0),(0,-1),(-1,0)]],r)[-1])(s+1)for s in range(6)]:
 for h in i:
  c,d=zip(*h);g=[[' ']*(M(d)-m(d)+1)for _ in[0]*(M(c)-m(c)+1)]
  for x,y in h:g[x-m(c)][y-m(d)]='#'
  *map(print,[''.join(r)for r in g]),;print()
