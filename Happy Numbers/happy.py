for i in range(201):
 k=i;exec("k=sum([int(d)**2 for d in'%s'%k]);"*9)
 if k==1:print(i)
