import sys
g=lambda a,b:b and[a//b]+g(b,a%b)or[]
for f in sys.argv[1:]:print(str(g(*map(int,f.split('/')))).replace(*',;',1))
