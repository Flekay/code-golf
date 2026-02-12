s=[1,2,2]
for i in range(2,1000):s+=[3-s[-1]]*s[i]
print(*s[:1000])
