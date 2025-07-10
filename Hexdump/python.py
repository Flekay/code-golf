import sys
P=print
for s in sys.argv[1:]:
	for i in range(0,len(s),16):
		P(f'{i:08x}: ',end='')
		for j in range(i,i+16):P(f"{ord(s[j]):02x}"if j<len(s)else'  ',end=['',' '][j%2])
		P('',s[i:i+16].replace('\n','.'))
	P()
