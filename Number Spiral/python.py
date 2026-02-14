R=range(10)
for r in R:print(*[f'{4*(L:=min(r,c,9-r,9-c))*(10-L)+(c-L if r==L else 9-3*L+r if c>8-L else 27-5*L-c if r>8-L else 36-7*L-r):2}'for c in R])
