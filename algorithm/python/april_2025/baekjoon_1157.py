import collections

S = input().upper()

cnt = collections.Counter(S)
ans = cnt.most_common(2)

if len(ans) > 1 and ans[0][1] == ans[1][1]:
    print('?')
else:
    print(ans[0][0])
