def h(n,a,b,c):
 if n:h(n-1,a,c,b);print(f"{a} -> {c}");h(n-1,b,a,c)
h(9,1,2,3)
