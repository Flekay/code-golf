for r in range(16):print(' '*(15-r)+' '.join(' ▲'[(r|c)<r+1]for c in range(r+1)))
