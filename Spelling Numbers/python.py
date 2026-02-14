import sys
w="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety".split()
s=lambda n:n>999and"one thousand"or n>99and w[n//100]+" hundred"+[""," and "+s(n%100)][n%100>0]or n>19and w[n//10+18]+["","-"+w[n%10]][n%10>0]or w[n]
for x in sys.argv[1:]:print(s(int(x)))
