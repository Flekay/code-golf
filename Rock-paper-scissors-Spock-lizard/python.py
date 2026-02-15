import sys
for a in sys.argv[1:]:x,y=[ord(c)%79%5for c in a];d=(x-y)%5;print(*d and[a[d%2],"poisons smashes cuts covers crushes eats vaporizes decapitates disproves crushes".split()[(x,y,x+5,y+5,x)[d]],a[~d%2]]or["Tie"])
