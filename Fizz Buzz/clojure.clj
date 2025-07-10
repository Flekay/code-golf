(doseq[i(range 1 101)](let[a(=(mod i 3)0)b(=(mod i 5)0)](println(str(if a"Fizz""")(if b"Buzz""")(if(or a b)""i)))))
