from decimal import*
getcontext().prec=n=1305
d=(3+Decimal(8).sqrt())**n/2
b,c,s=-d/d,-d,0
for k in range(n):j=k-~k;c=b-c;s+=c/j/j;b=b*2*(k*k-n*n)/j/-~k
print(str(s/d)[:1002])
