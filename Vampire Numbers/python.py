S,R=sorted,range(10,1001)
print(*S({i*j for i in R for j in R if~len(f:=S(f'{i}{j}'))%2and j%10+i%10and S(f'{i*j}')==f}),sep='\n')
