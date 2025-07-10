[print(i)for i in range(201)if sum(j*(i%j<1)for j in range(1,i))>i]
