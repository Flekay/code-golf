import sys
for a in sys.argv[1:]:
 n,d=map(int,a.split('/'));r=n%d;s=str(n//d)+'.'[:r];S={}
 while r*(r not in S):S[r]=len(s);r*=10;s+=str(r//d);r%=d
 if r:s=f'{s[:S[r]]}({s[S[r]:]})'
 print(s)
