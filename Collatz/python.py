for i in range(1,1001):
 b=0
 while i>1:i=[i//2,i*3+1][i%2];b+=1
 print(b)
