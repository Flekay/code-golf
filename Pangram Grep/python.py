import sys
[print(i)for i in sys.argv if{*map(chr,range(97,123))}<={*i.lower()}]
