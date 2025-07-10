i=1
while i<1e4:d=[j for j in range(1,i+1)if i%j<1];sum(d)%len(d)or print(i);i+=1
