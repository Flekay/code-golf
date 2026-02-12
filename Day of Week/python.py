import sys,datetime as d
for x in sys.argv[1:]:print(f"{d.date.fromisoformat(x):%A}")
