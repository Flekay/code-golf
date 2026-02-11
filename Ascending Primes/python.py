c={int(''.join(str(q+1)for q in range(9)if i>>q&1))for i in range(2,512)}
for n in sorted(c):all(n%p for p in range(2,int(n**.5)+1))and print(n)
