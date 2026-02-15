import sys
for a in sys.argv[1:]:
 s=p=j=0;A=B=D=1
 for c in a:
  if c>" ":B+=c in"X/"*(j<27);D+=c in"X"*(j<27);p=10-p*(c<"X")if c in"X/"else int(c)if"/"<c<":"else ord(c)%9311*(c>"~");s+=A*p;A=B;B=D;D=1
  j+=1
 print(s)
