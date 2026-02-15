import sys
for n in sys.argv[1:]:print(''.join([o*(e:=int(d)),o+f,f+o*(e-5),o+t][e//5+-~e//5]for d,o,f,t in zip(n.zfill(4),'MCXI',' DLV',' MCX')))