import sys;S,P,D,L,H='✂📄💎🦎🖖'
r={S+P:"cuts",P+D:"covers",D+L:"crushes",L+H:"poisons",H+S:"smashes",S+L:"decapitates",L+P:"eats",P+H:"disproves",H+D:"vaporizes",D+S:"crushes"}
for a in sys.argv[1:]:print("Tie"if a[0]==a[1]else f"{a[0]} {r[a]} {a[1]}"if a in r else f"{a[1]} {r[a[::-1]]} {a[0]}")
