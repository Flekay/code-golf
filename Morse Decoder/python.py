import sys
h,d,x,r='-. ▄'
k={d+h:'A',h+d*3:'B','-.-.':'C',h+d+d:'D',d:'E','..-.':'F',h+h+d:'G',d*4:'H',d*2:'I',d+h*3:'J',h+d+h:'K','.-..':'L',h*2:'M',h+d:'N',h*3:'O','.--.':'P','--.-':'Q',d+h+d:'R',d*3:'S',h:'T',d+d+h:'U',d*3+h:'V',d+h*2:'W','-..-':'X','-.--':'Y','--..':'Z'}
for n in range(10):k[h*(n-5)+d*(n if n<5else 5-n%5)+h*(5-n)]=str(n)
print(x.join(''.join(k[i.replace(r*3,h).replace(r,d).replace(x,'')]for i in w)for w in[z.split(x*3)for z in sys.argv[1].split(x*10)]))
