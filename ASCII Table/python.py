z=range
y=z(2,8)
print("  ",*y,'\n',13*"-")
for i in z(16):print("%X:"%i,*[[chr(r*16+i),'DEL'][r*i>104]for r in y])
