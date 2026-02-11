import fractions as f
for i in f.sys.argv[1:]:print('%d/%d'%f.Fraction(i).as_integer_ratio())
