import sys
for n in sys.argv[1:]:
	n=n.split('\n');S=n[0].split();G=n[1:-1];I=n[-1][1:-1];g={};A=p=''
	for w in G:
		g[R:=w[2]]=w[4:].split()
		if w[0]=='>':p=R
		if w[1]=='F':A+=R
	for i in I:p=g[p][S.index(i)]
	print(p,['Reject','Accept'][p in A])
