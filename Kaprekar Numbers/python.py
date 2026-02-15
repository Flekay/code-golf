*map(print,sorted({n for d in range(1,9)for n in range(1,min(10**d,25000001))if~-n*n%(10**d-1)<1})),
