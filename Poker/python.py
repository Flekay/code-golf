import sys;Z="Straight"
for a in sys.argv[1:]:Y,X,M,V,W=s=sorted((r:=ord(c)%16)-(r>12)for c in a);A=len({ord(c)>>4for c in a})<2;L=len({*s});ST=L>4and(W-Y<5or X-Y>8);print(A*ST*([Z,"Royal"][X>9>Y]+" Flush")or(L<3)*["Full House","Four of a Kind"][X==V]or A*"Flush"or ST*Z or(s.count(M)>2)*"Three of a Kind"or["High Card","Pair","Two Pair"][5-L])
