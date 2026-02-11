r=[1]
for _ in range(20):
 print(*r)
 p=[0,0]+r+[0,0]
 r=[p[i]+p[i+1]+p[i+2]for i in range(len(p)-2)]
