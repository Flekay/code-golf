for i in(R:=range(2,999)):
	if(I:=int(str(i)[::-1]))!=i and all((i%j+(i==j))and((I==j)+I%j)for j in R):print(i)
