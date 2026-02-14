import sys;Z="Straight";K=" of a Kind"
for a in sys.argv[1:]:Y,X,M,V,W=s=sorted((r:=ord(c)%16)-(r>12)for c in a);L=len({*s});ST=L>4and(W-Y<5or X-Y>8);print((max(a)<chr(ord(min(a))|15))*(ST*([Z,"Royal"][X>9>Y]+" ")+"Flush")or(L<3)*["Full House","Four"+K][X==V]or ST*Z or["High Card","Pair","Two Pair","Three"+K][5-L+s.count(M)//3])
