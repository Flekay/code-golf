Q=[((0,0),)]
for p in Q:
 if len(p)<6:
  for c in{(x+d%3-1,y+d//3-1)for x,y in p for d in(1,3,5,7)}-{*p}:
   n=*p,c;X,Y=zip(*n);c=(*sorted((a-min(X),b-min(Y))for a,b in n),);Q+=[c][c in Q:]
 X,Y=zip(*p);[print(''.join(' #'[(x,y)in p]for y in range(-~max(Y))))for x in range(-~max(X))];print()
