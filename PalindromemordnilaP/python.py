import sys
for s in sys.argv[1:]:print([s+s[:i][::-1]for i in range(len(s))if s[i:]==s[i:][::-1]][0])
