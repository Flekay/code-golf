R=range;s,v,d,c=' │╱█'
for z in R(1,8):W=s*z;H,V=c+'─'*z*4+c,v+W*4+v;*map(print,[s+W+H,*[W[i:]+d+W*4+d+s*i+v for i in R(z)],H+W+v,*[V+W+v]*~-z,V+W+c,*[V+W[i+1:]+d for i in R(z)],H,'']),
