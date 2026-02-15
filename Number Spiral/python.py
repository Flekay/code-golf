g={};p=0;d=1;R=range(10)
exec("g[p]=len(g)\nif(n:=p+d)in g or{n.real,n.imag}-{*R}:d*=1j\np+=d;"*100)
for r in R:print(*['%2d'%g[r*1j+c]for c in R])