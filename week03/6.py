num = [int(s) for s in input().split()]
was= set()
for i in num:
    if i in was:
        print(i,'YES')
    else:
        print(i,'NO')
        was.add(i)
