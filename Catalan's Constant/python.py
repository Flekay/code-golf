n=1890;a,b=3,1
exec("a,b=b,6*b-a;"*n+"D=b;b=10**n;c=D*b;s=k=0;"+"j=k-~k;c=b-c;s+=c//j//j;b=b*2*(k*k-n*n)//j//-~k;k+=1;"*n)
print(f"0.{-s//D}"[:1002])
