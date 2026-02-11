import re
o='1'
for _ in[0]*20:print(o);o=re.sub(r'(.)\1*',lambda m:str(len(m[0]))+m[1],o)
