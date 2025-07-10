import sys
h,d,x,r='-. ▄'
k={'A':d+h,'B':h+d*3,'C':'-.-.','D':h+d+d,'E':d,'F':'..-.','G':h*2+d,'H':d*4,'I':d*2,'J':d+h*3,'K':h+d+h,'L':'.-..','M':h*2,'N':h+d,'O':h*3,'P':'.--.','Q':'--.-','R':d+h+d,'S':d*3,'T':h,'U':d*2+h,'V':d*3+h,'W':d+h*2,'X':'-..-','Y':'-.--','Z':'--..'}
for n in range(10):k[str(n)]=h*(n-5)+d*(n if n<5else 5-n%5)+h*(5-n)
for s in sys.argv[1:]:print((x*10).join(['   '.join([x.join([*k[c]]).replace(d,r).replace(h,r*3)for c in w])for w in s.split()]))
