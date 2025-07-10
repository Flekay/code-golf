for i in range(3321):
 z=c=i%81*.03125-2+1j*(i//81*.05-1);n=1064
 while n and abs(z)<=2:z=z*z+c;n-=1
 print("█▒"[abs(z)>2],end="\n"[i%81<80:])
