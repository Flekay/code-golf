import sys
x=y=0
for i in sys.argv[1:]:d=b"0644444444157344286028"[ord(i)%262%22];x+=d//3-17;y+=d%3-1;print(x,y)
