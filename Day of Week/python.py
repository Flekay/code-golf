import sys,datetime as d
for x in sys.argv[1:]:print(d.date(*map(int,x.split('-'))).strftime('%A'))
