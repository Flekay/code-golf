Q=[((0,0),)]
for p in Q:
 if len(p)<6:
  for c in{(x+a,y+b)for x,y in p for a,b in((0,1),(1,0),(0,-1),(-1,0))}-{*p}:
   n=*p,c;X,Y=zip(*n);c=(*sorted((a-min(X),b-min(Y))for a,b in n),)
   if c not in Q:Q+=c,
 X,Y=zip(*p);[print(''.join(' #'[(x,y)in p]for y in range(max(Y)+1)))for x in range(max(X)+1)];print()
