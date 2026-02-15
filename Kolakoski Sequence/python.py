s=1,2,2
for i in range(2,999):s+=(i%2+1,)*s[i]
print(*s[:1000])
