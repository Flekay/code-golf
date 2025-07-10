import sys,math
for i in sys.argv[1:]:x,y=map(int,i.split('/'));g=math.gcd(x,y);print(f'{x//g}/{y//g}')
