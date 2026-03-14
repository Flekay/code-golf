import sys
for s in sys.argv[1:]:l=s.split();a,b,c=map([*map(l.index,l)].count,(0,1,2));print('1💎 '*(a<2)+f'{a}🥇'+f' {b}🥈'*(b>0)+f' {c}🥉'*(c>0))
