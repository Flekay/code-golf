import sys;R=range;p=print
_,*b=map(list,sys.argv)
def s():
 for q in R(81):
  if(w:=b[q//9])[c:=q%9]>'9':
   for w[c]in{*str(5**18)}-{*w}-{z[c]for z in b}-{b[q//27*3+i//3][c-c%3+i%3]for i in R(9)}:s()
   w[c]='_';return
 for i in R(10):a,h,c,d,e,*_=[chr(9436+c)for c in b"3%SW7D$`fLG%coO;%[_?"[(i**8%51%21%5)*5:]];p(a+d.join([(h*3+c)*2+h*3]*3)+e);p('┃'+' %s │ %s │ %s ┃'*3%(*b[i],))
s()
