import sys
x=y=0
for i in sys.argv[1:]:x+=(i in'↘↳⇘→⇒⇨↗↱⇗')-(i in'↙↲⇙←⇐⇦↖↰⇖');y+=(i in'↖↰⇖↑⇑⇧↗↱⇗')-(i in'↙↲⇙↓⇓⇩↘↳⇘');print(x,y)
