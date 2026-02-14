import sys
for g in sys.argv[1:]:print(next((p for p,M in zip('XO',[[[c==t for c in r]for r in g.split()]for t in'XO'])if any(map(all,M+[*zip(*M),*[[M[i][(i,2-i)[d]]for i in(0,1,2)]for d in(0,1)]]))),'-'))
