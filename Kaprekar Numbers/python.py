S={1};k=9
while k<1e8:
 for n in range(2,min(k+1,25000001)):
  if(n*n-n)%k<1:S|={n}
 k=k*10+9
print(*sorted(S),sep="\n")
