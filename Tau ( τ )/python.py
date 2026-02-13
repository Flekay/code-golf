s=p=10**1006;k=0
while p:k+=1;p=p*k//(k-~k);s+=p
print('6.'+str(4*s)[1:-6])
