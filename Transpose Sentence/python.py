import sys
from itertools import*
for a in sys.argv[1:]:print(*map(''.join,zip_longest(*a.split(),fillvalue='')))
