def justifyWords(words,width):
 s=1
 if len(words)>1 and width>0:
  c=0
  for word in words:
   c+=len(word)
  s=(width-c)//(len(words)-1)
  d=width-c-(len(words)-1)*s
  for n in range(d):
   words[n]+=' '
 print(*words,sep=s*' ')

def doLine(words,width):
 i=0
 c=-1
 subw = []
 w = ''
 while i < len(words) and c+len(words[i])<width:
  w = words[i]
  subw += [w]
  c += len(w)+1
  i+=1
 justifyWords(subw,0if len(words)==i else width)
 return words[i:]

import sys
for arg in sys.argv[1:]:
 lines = arg.split('\n')
 s = lines[0].split(' ')
 indent = int(s[0])
 width = int(s[1])
 n = 1
 for line in lines[1:]:
  words = line.split(' ')
  while len(words) > 0:
   print(indent*' ',end='')
   words = doLine(words,width)
   n+=1;indent -= n%2;width += n%2*2
  n+=1;indent -= n%2;width += n%2*2;print()
