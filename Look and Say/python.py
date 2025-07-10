o='1'
for _ in[0]*20:
 s=[*o];print(o);o,t,p='',0,s[0]
 for x in s:
  if x==p:t+=1
  else:o+=f'{t}{p}';t=1;p=x
 o+=f'{t}{p}'
