from operator import itemgetter

N = int(input())
pnt_list = []
for i in range(N):
    pnt_list.append([int(w) for w in input().split()])


ans = sorted(pnt_list, key=itemgetter(0,1))

for i in range(N):
    print(str(ans[i][0]) + " " + str(ans[i][1]))