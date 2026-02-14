j=255;t=[];x=1;exec("t+=x,;x^=x*2^(x>>7)*283;"*256)
S=[99]+[0]*j
for i in range(j):S[t[i]]=((x:=t[~i]*257)^x>>4^x>>5^x>>6^x>>7^99)&j
for i in range(16):print('%02x '*16%(*S[16*i:][:16],))
