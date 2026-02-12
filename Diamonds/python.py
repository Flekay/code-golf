z=range
[print(' '*(11-r)+str((10**r//90)**2or''))for i in z(2,11)for r in[*z(2,i),*z(i,0,-1)]]
