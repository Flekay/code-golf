S,R=sorted,range(10,1001)
*map(print,S({i*j for i in R for j in R if~len(f:=S(f'{i}{j}'))%2*(j%10|i%10)and S(f'{i*j}')==f})),
