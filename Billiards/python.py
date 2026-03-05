import sys,math
for a in sys.argv[1:]:
 H,W=map(int,a.split());G=2*math.gcd(W,H)
 for r in range(-~H):t=[' ']*G;t[r%G],t[~r%G]='\\/';print(''.join(t*W)[:W*(r<H)])
