R=range
for z in R(1,8):x=z*4;s,h,v,d,c=' ─│╱█';H,V=c+h*x+c,v+s*x+v;*map(print,[s*-~z+H,*[s*(z-i)+d+s*x+d+s*i+v for i in R(z)],H+s*z+v,*[V+s*z+v]*~-z,V+s*z+c,*[V+s*(z+~i)+d for i in R(z)],H,'']),
