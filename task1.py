n = int(input())
m = int(input())
tip1 = m * [int(a) for a in range(1, n + 1)]
tip2 = [' ']
tip3 = []
cnt = 0
while tip2[-1] != 1:
    tip2.clear()
    for j in range(cnt, m + cnt):
        tip2.append(tip1[j])
        cnt += 1
    tip2_copy = tip2.copy()
    tip3.append(tip2_copy)
    cnt -= 1
for f in range(len(tip3)):
    print(tip3[f][0], end='')
