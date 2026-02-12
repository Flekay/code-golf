for i in range(3321):
 z=c=i%81/32-2+1j*(i//81/20-1);n=1064
 while n and abs(z)<=2:z=z*z+c;n-=1
 print("█▒"[abs(z)>2],end="\n"[i%81<80:])
