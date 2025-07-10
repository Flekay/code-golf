import sys
for s in sys.argv[1:]:d=-sum((10-i)*int(c)for i,c in enumerate(s.replace('-','')))%11;print(s+f'X{d}'[d<10])
