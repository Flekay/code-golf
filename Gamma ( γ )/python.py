from decimal import*
getcontext().prec=a=1005;t=S=e=Decimal(1);h=T=0;k=1
while k<a*3:t=t*a*a/k/k;h+=e/k;S+=t;T+=t*h;k+=1
print(str(T/S-(a*e).ln())[:-4])
