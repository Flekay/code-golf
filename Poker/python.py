import sys
for a in sys.argv[1:]:
 s=sorted((r:=ord(c)%16)-(r>12)for c in a);A=len({ord(c)//16for c in a})<2;L=len({*s});ST=L>4and(s[4]-s[0]==4or s[1]-s[0]>8)
 print((("Royal"if s[1]>9>s[0]else"Straight")+" Flush")if A*ST else("Four of a Kind"if s[1]==s[3]else"Full House")if L<3else"Flush"if A else"Straight"if ST else"Three of a Kind"if s.count(s[2])>2else"Two Pair"if L<4else"Pair"if L<5else"High Card")
