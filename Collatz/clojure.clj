(doseq[i(range 1 1001)](prn(loop[j 0 n i](if(= n 1)j(recur(inc j)(if(odd? n)(+(* n 3)1)(/ n 2)))))))
