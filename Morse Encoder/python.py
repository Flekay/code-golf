import sys
print(end="".join([" "*7,bin("..ETIANMSURWDKGOHVF.L.PJBXCYZQ..54.3...2.......16.......7...8.90".find(c))[3:].translate({48:"▄ ",49:"▄"*3+" "})+"  "][c>" "]for c in sys.argv[1])+" "*7)
