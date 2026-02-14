import itertools as I,sys
for a in sys.argv[1:]:c=a.split();[all(len({x[f]for x in t})%2for f in range(4))and print(*t)for t in I.combinations(c,3)]
