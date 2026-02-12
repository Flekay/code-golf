from decimal import*
getcontext().prec=a=1005
e=Decimal(1)
t=S=e
h=T=e-e
for k in range(1,a*3):t=t*a*a/k/k;h+=e/k;S+=t;T+=t*h
print(str(T/S-(a*e).ln())[:-4])
