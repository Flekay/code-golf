import sys
d={"/":"\n"}
for i in range(12):d.update({"KQRBNPkqrbnp"[i]:chr(9812+i),str(i):" "*i})
for a in sys.argv[1:]:
 for c in a.split(" ")[0]:print(d[c],end="")
 print("\n")
