li = []

with open("./dict.csv", "r", encoding="utf-8") as f:
    file_data = f.readlines()
    for i in file_data:
        li.append(i.split('\n')[0])

best = [[] for i in range(5)]
ans = []
moji = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモマミムメモヤユヨワヲン'
print(len(moji))
for i in range(5):
    for k in range(46):
        tmp = 0
        for text in li:
            if text[i] == moji[k]:
                tmp += 1
        best[i].append(tmp)
    print(best[i])
    max_p = best[i].index(max(best[i]))
    ans.append(moji[max_p])
print(ans)
