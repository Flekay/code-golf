Q=[[(0,0)]]
for p in Q:
 for c in{(x+d%3-1,y+d//3-1)for x,y in p for d in(1,3,5,7)}-{*p}:a,b=min(n:=p+[c]);c=sorted((x-a,y-b)for x,y in n);Q+=[c][c in Q:len(p)<6]
 X,Y=zip(*p);[print(''.join(' #'[(x,y)in p]for y in range(min(Y),-~max(Y))))for x in range(-~max(X))];print()
