r=range(2,99);*map(print,sorted({x**y+y**x for x in r for y in r})[:107]),
