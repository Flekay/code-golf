import sys
w="zero one two three four five six s! eight nine ten el! twelve thir@four@fif@six@s!@eigh@nine@twen$thir$for$fif$six$s!$eigh$nine$".translate({64:'teen ',36:'ty ',33:'even'}).split()
s=lambda n:n>999and"one thousand"or n>99and w[n//100]+" hundred"+(" and "+s(m:=n%100))*(m>0)or n>19and w[n//10+18]+("-"+w[n%10])*(n%10>0)or w[n]
for x in sys.argv[1:]:print(s(int(x)))
