i=0
while i<1e4:i+=1;d=[j for j in range(i)if i%-~j<1];sum(d)%len(d)or print(i)
