for i in range(3321):
 z=c=i%81/32-2+i//81*.05j-1j;n=2e3
 while n*(abs(z)<3):z=z*z+c;n-=1
 print("█▒"[n>0],end=i%81//80*"\n")
