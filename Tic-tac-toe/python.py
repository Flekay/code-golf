import sys
for g in sys.argv[1:]:print(next((p for p in'XO'if p*3in[g[:3],g[4:7],g[8:],g[::4],g[1::4],g[2::4],g[::5],g[2:9:3]]),'-'))
