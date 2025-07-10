c={int(''.join(str(q+1)for q in range(d)if i>>q&1))for d in range(10)for i in range(1,1<<d)}
for n in sorted(c)[1:]:all(n%p for p in range(2,int(n**.5)+1))and print(n)
