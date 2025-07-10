import sys
[print(i)for i in sys.argv if all(chr(x+97)in i.lower()for x in range(26))]
