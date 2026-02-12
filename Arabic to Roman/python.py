import sys
for n in sys.argv[1:]:print(''.join([o*(e:=int(d)),o+f,f+o*(e-5),o+t][e//5*2+e%5//4]for d,o,f,t in zip('%04d'%int(n),'MCXI',' DLV',' MCX')))
