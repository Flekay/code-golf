for i in(R:=range(2,999)):((I:=int(str(i)[::-1]))-i)*all((i%j+(i==j))and((I==j)+I%j)for j in R)and print(i)
