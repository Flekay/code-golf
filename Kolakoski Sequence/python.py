s=[1,2,2]
[s.extend([1if s[-1]>1else 2]*s[i])for i in range(2,1000)]
print(*s[:1000])
