import sys
for r in sys.argv[1:]:
 t=p=0
 for c in r[::-1]:v=5**((q:='IVXLCDM'.find(c))%2)*10**(q//2);t+=v-2*v*(v<p);p=v
 print(t)
