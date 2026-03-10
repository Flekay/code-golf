for i in(R:=range(2,9999)):((I:=int(str(i)[::-1]))-i)*all((i%j)*(I%j)or j in(i,I)for j in R)and print(i)
