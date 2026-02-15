P=k=1;s='';exec("k+=1\nif P%k:n=1000;c=0;exec('n//=k;c+=n;'*9);s+='*%d'%k+'^%d'%c*(c>1)\nP*=k*k;"*999)
print(s[1:])