import sys
s=[]
for l in sys.argv[1:]:
 for o in l.split():s+=[o]if'/'<o else[eval(f"{s.pop(-2)}{o}{s.pop()}")]
 print(int(s[-1]))
