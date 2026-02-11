s=[1,2,2]
[s.extend([3-s[-1]]*s[i])for i in range(2,1000)]
print(*s[:1000])
