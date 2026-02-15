import sys
for a in sys.argv[1:]:print(chr(128001+ord("ȜȠ  Ț ȍț   Ȓ     ȵȔ ɀȡԏ ȏȅ  ȄɁȁȲȈ ~  ǿȖ   ȭȇȎ Ȇ"[(3*ord(a[0])+9*ord(a[-1])+len(a))%47])))
