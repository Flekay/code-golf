import sys;R=range;p=print
def s(g):
 for r in R(9):
  w=g[r]
  for c in R(9):
   if w[c]<1:
    for n in R(1,10):
     if{n}-{*w,*[g[i][c]for i in R(9)],*[g[r-r%3+i//3][c-c%3+i%3]for i in R(9)]}:
      w[c]=n
      if s(g):return 1
    w[c]=0;return
 return 1
s(b:=[[ord(c)%48%47 for c in r]for r in sys.argv[1:]])
f=lambda a,b,c,d,e:a+((y:=((x:=b*3)+c)*2+x)+d)*2+y+e
S='┏━┯┳┓┠─┼╂┨┣━┿╋┫┗━┷┻┛'
V='┃'+(' %d │'*2+' %d ┃')*3
p(f(*S[:5]))
for i in R(9):p(V%(*b[i],));p(f(*S[15*(i>7)or(i%3>1)*5+5:][:5]))
