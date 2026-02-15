import calendar as c
for a in c.sys.argv[1:]:print(c.month(*map(int,a.split()[::-1])).split('\n',1)[1])