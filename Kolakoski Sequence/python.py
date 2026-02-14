s=1,2,2
for i in range(2,999):s+=(s[-1]^3,)*s[i]
print(*s[:1000])
