r=range(1,101)
for i in r:print(*[d for d in r if i%d<1])
