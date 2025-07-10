S,R=sorted,range(10,1001)
print(*S({i*j for i in R for j in R if len(f:=S(str(i)+str(j)))%2<1 and (i%10 or j%10) and S(str(i*j))==f}),sep='\n')
