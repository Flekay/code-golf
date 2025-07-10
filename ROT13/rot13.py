import codecs,sys
for a in sys.argv[1:]:print(codecs.encode(a,'rot13'))
