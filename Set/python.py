import sys
for a in sys.argv[1:]:
 c=a.split()
 for i in range(12):
  for j in range(i+1,12):
   for k in range(j+1,12):
    if all(len({c[i][f],c[j][f],c[k][f]})!=2 for f in range(4)):print(c[i],c[j],c[k])
