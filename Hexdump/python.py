import sys
for s in sys.argv[1:]:
 for i in range(0,len(s),16):c=s[i:i+16];h=c.encode().hex()+' '*32;print('%08x:'%i,' '.join(h[k:k+4]for k in range(0,32,4)),'',c.replace('\n','.'))
 print()
