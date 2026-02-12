for r in range(16):print(*(' '*(15-r-c*15)+' ▲'[~r&c<1]for c in range(r+1)))
