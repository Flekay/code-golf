import sys
s="..ETINAMSDRGUKWOHBLZFCP.VX.Q.YJ.56.7...8.......94.......3...2.10"
for w in sys.argv[1].split(" "):
 for c in w:print(bin(s.index(c))[3:][::-1].replace("0","▄ ").replace("1","▄"*3+" ")," ",end="")
 print(" "*7,end="")
