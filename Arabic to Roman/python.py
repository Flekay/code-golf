import sys
for i in sys.argv[1:]:
	s,i='',int(i)
	for a,r in zip([1000,900,500,400,100,90,50,40,10,9,5,4,1],'M CM D CD C XC L XL X IX V IV I'.split()):x=i//a;s+=x*r;i-=a*x
	print(s)
