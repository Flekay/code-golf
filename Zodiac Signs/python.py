import sys
j=20;r=range
l=[[*r(100*i+j,100*(i+1)+(j:=j+[-1,2,-1,1,1,1,0,0,0,0,-1][i]))]for i in r(11)]+[[*r(1300)]]
for a in sys.argv[1:]:a,b,_,c,d,_,e,f,*_=a;i=[(int(a+b)-1)*100+int(c+d)in o for o in l].index(1)-2;j=i+int(e+f)//2-2;print(chr(i%12+9800)+chr(j%12+9800)*(i!=j))
