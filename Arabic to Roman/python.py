import sys
for n in sys.argv[1:]:print(''.join([o*e,o+f,f+o*(e-5),o+t][e//5+-~e//5]for e,o,f,t in zip(map(int,n.zfill(4)),'MCXI',' DLV',' MCX')))
