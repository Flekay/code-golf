import itertools as I,sys
for a in sys.argv[1:]:c=a.split();[all(len(s)%2for s in map(set,zip(*t)))and print(*t)for t in I.combinations(c,3)]
