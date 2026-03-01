s='A';exec("s=s.translate({65:'+BF-AFA-FB+',66:'-AF+BFB+FA-'});"*5)
g=eval('[0]*63,'*63);x=v=0;u=1;y=62
for c in s:
 if'E'<c:d=1<<v*v-u-~v;g[y][x]|=d;g[y+v][x+u]=d*5%15;x+=u+u;y+=v+v;g[y][x]|=d*4%15
 if'.'>c:k=44-ord(c);u,v=v*k,-u*k
for r in g[::2]:print(''.join(' A╵└A─┘AA┌│A┐'[c]for c in r))
