import sys
for a in sys.argv[1:]:
 c=a.split()
 [all(len({c[x][f]for x in(i,j,k)})%2for f in range(4))and print(c[i],c[j],c[k])for i in range(12)for j in range(i+1,12)for k in range(j+1,12)]
