t=1,;exec("t+=max(j*(t[-i:]*j==t[-i*j:])for i in range(len(t))for j in range(5)),;"*999)
*map(print,t),
