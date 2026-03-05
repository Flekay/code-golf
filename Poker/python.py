import sys;Z="Straight";K=" of a Kind"
for a in sys.argv[1:]:Y,X,*_,W=s=sorted(ord(c)%16for c in a);S=W-Y<5+W//13or X-Y>8;print(max(a)<chr(ord(min(a))|15)and[Z+" ","Royal "][X>9>Y]*S+"Flush"or("Pair","Full House",Z*S or"High Card","Three"+K,"Four"+K,"Two Pair")[-sum(map(s.count,s))%7])
