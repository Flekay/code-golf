import sys
for n in sys.argv[1:]:print(n+"tsnrhtdd"[(v:=int(n))%5*(v%100^15>4>v%10)::4])
