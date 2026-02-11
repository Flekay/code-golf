import sys
[print(i)for i in sys.argv if{*'abcdefghijklmnopqrstuvwxyz'}<={*i.lower()}]
