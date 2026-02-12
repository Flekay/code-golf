from decimal import*
getcontext().prec=1005
a=p=Decimal(1);b=(a/2).sqrt();t=a/4
exec('x=(a+b)/2;b=(a*b).sqrt();t-=p*(a-x)**2;a=x;p*=2;'*9)
print(str((a+b)**2/t/2)[:-4])
