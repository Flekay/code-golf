print(*sorted({n for k in[10**d-1 for d in range(1,9)]for n in range(1,min(k+1,25000001))if(n*n-n)%k<1}),sep="\n")
