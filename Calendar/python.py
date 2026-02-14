import calendar as c
for a in c.sys.argv[1:]:
 m,y=map(int,a.split());print("Mo Tu We Th Fr Sa Su")
 for w in c.monthcalendar(y,m):print(*(f'{d or"":2}'for d in w))
 print()
