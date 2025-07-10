from decimal import*
s=[0,1,1]
[s.extend([0if s[-1]>0else 1]*(s[i]+1))for i in range(2,2500)]
getcontext().prec=999
print(f'{Decimal(int(b:=''.join(map(str,s[1:])),2))/2**len(b)}4')
