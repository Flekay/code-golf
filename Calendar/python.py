import sys,calendar
for i,a in enumerate(sys.argv[1:]):
 if i:print()
 m,y=map(int,a.split())
 print("Mo Tu We Th Fr Sa Su")
 for w in calendar.monthcalendar(y,m):
  print(*(f'{d:2}'if d else'  'for d in w))
