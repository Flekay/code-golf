import sys;R=range;p=print
S=''.join(chr(9436+c)for c in b"3%SW7D$`fLG%coO;%[_?")
V='┃'+' %d │ %d │ %d ┃'*3
b=[[ord(c)%48%47for c in r]for r in sys.argv[1:]]
def s():
 for q in R(81):
  if(w:=b[q//9])[c:=q%9]<1:
   for n in R(1,10):
    if{n}-{*w}-{z[c]for z in b}-{b[q//27*3+i//3][c-c%3+i%3]for i in R(9)}:w[c]=n;s()
   w[c]=0;return
 for i in R(10):p((t:=S[(877972>>i*2&3)*5:][:5])[0]+t[3].join([t[2].join([t[1]*3]*3)]*3)+t[4]);i<9!=p(V%(*b[i],))
 1/0
s()