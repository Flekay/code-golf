import sys
for a in sys.argv[1:]:
 n,d=map(int,a.split('/'));r=n%d;s=str(n//d)+'.'[:r];S={}
 while r*(r not in S):S[r]=s;r*=10;s+=str(r//d);r%=d
 if r:s=S[r]+'('+s[len(S[r]):]+')'
 print(s)
