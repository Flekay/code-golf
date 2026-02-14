import sys
for s in sys.argv[1:]:
 i=0
 while s[i:]!=s[i:][::-1]:i+=1
 print(s+s[:i][::-1])
