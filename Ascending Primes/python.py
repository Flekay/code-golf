s=[0]
for d in range(9):s+=[10*x-~d for x in s]
for n in sorted(s[2:]):pow(2,n,n)==2%n!=print(n)
