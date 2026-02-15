import sys
for n in sys.argv[1:]:j=1;sum(((d:=int(c))*2%9or d,d)[j:=1-j]for c in n if c>' ')%10or print(n)
