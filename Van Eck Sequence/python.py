x=[0]
for _ in x*1000:r=x[-1];print(r);x+=[0if r not in x[:-1]else x[::-1][1:].index(r)+1]
