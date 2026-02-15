b='11';i=2;exec("b+=str(i%2)*-~int(b[i-1]);i+=1;"*4**6);print(f'0.{int(b,2)*10**1000>>len(b)}')
