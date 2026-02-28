a=lambda i,c="n":f"{i or c+'o more'} bottle{'s'[:i^1]} of beer on the wall";z=99
while~z:print(f"{a(z,'N')}, {a(z)[:-12]}.\n{'GToa kteo  otnhee  dsotwonr ea nadn dp absusy  isto maer omuonrde'[z>0::2]}, {a(~-z%100)}.\n");z-=1
