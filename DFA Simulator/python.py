import sys
for a in sys.argv[1:]:
 a=a.split("\n");R=[_[1:].split()[0][-1]for _ in a[1:-1]];y=R[['>'in i for i in a].index(1)-1]
 for x in a[-1][1:-1]:y=a[R.index(y)+1][a[0].index(x)]
 print(y,"Accept"if"F"in a[R.index(y)+1]else"Reject")
