import calendar as c
for i,a in enumerate(c.sys.argv[1:]):
 if i:print()
 m,y=map(int,a.split())
 print("Mo Tu We Th Fr Sa Su")
 for w in c.monthcalendar(y,m):
  print(*(f'{d:2}'if d else'  'for d in w))
