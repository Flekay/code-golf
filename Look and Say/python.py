import re;s='1';exec("print(s);s=re.sub(r'(.)\\1*',lambda m:str(len(m[0]))+m[1],s);"*20)
