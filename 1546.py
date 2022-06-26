n = int(input())

avg = 0
maxscore = 0


aa = list(map(int, input().split()))
maxscore = max(aa)


for i in range(n) :
    aa[i] = (aa[i] / maxscore) * 100
    avg += aa[i]

avg = avg / n
print(format(avg, ".2f"))

