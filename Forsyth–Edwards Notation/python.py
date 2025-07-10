import sys
for f in sys.argv[1:]:*map(print,[''.join('♜♞♝♛♚♟♖♘♗♕♔♙'[u.index(c)]if c in(u:='rnbqkpRNBQKP')else' '*int(c)for c in r)for r in f.split()[0].split('/')]+['']),
