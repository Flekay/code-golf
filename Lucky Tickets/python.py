import itertools as I,collections as C,sys
for a in sys.argv[1:]:d,b=map(int,a.split());print(sum(v*v for v in C.Counter(map(sum,I.product(*[range(b)]*(d//2)))).values()))
