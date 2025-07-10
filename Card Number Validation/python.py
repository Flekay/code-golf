import sys
for n in sys.argv[1:]:q=n.replace(' ','');(sum(sum(map(int,str(int(i)*2)))for i in q[::2])+sum(int(i)for i in q[1::2]))%10<1==print(n)
