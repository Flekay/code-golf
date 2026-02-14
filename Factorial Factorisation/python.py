P=1;s=''
for k in range(2,1001):
 if P%k:c=0;q=k;exec("c+=1000//q;q*=k;"*9);s+='*%d'%k+"^%d"%c*(c>1)
 P*=k*k
print(s[1:])
