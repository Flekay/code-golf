import sys
for a in sys.argv[1:]:
 n,d=map(int,a.split('/'));r=n%d;s=str(n//d)+'.'[:r];S={}
 while{r}-{*S,0}:S[r]=s;r*=10;s+=str(r//d);r%=d
 print(r and S[r]+f'({s[len(S[r]):]})'or s)
