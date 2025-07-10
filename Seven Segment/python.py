import sys
*map(print,[''.join(((U:=" _ ","| |",u:="|_|"),(S:=" "*3,r:="  |",r),(U,R:=" _|",L:="|_ "),(U,R,R),(S,u,r),(U,L,R),(U,L,u),(U,r,r),(U,u,u),(U,u,R))[g][x]for g in map(int,sys.argv[1]))for x in(0,1,2)]),
