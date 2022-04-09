import copy

li = []
bit = [0,0,0,0,0]

with open("./dict.csv", "r", encoding="utf-8") as f:
    file_data = f.readlines()
    for i in file_data:
        li.append(i.split('\n')[0])

tmp_li = copy.deepcopy(li)

def search_max(li):
    best = [[] for _ in range(5)]#それぞれ何回出現するか
    ans = [[] for _ in range(5)]#順位
    moji = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモマミムメモラリルレロヤユヨワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポァィゥェォッャュョヮー'
    mojilen = len(moji)
    for i in range(5):
        for k in range(mojilen):
            tmp = 0
            for text in li:
                if text[i] == moji[k]:
                    tmp += 1
            best[i].append(tmp)
        s_tmp = best[i]
        s_tmp = sorted(s_tmp, reverse=True)
        for t in range(mojilen):
            p = best[i].index(s_tmp[t])
            ans[i].append(moji[p])
    word = ''
    sum_beet = [sum(best[i]) for i in range(5)]
    weight = [[] for _ in range(5)]
    for i in range(5):
        for k in range(len(best[i])):
            x = (best[i][k]-min(best[i]))/(max(best[i])-min(best[i]))
            weight[i].append(x)
    
    assesment = []
    for text in li:
        sp = 0
        for i in range(5):
            #try:
            sp += weight[i][moji.index(text[i])]
            #except 
        assesment.append(sp)
    best_ans = []
    for a in assesment:
        try:
            x = (a-min(assesment))/(max(assesment)-min(assesment))
            best_ans.append(x)
        except ZeroDivisionError:
            return None

    asses_tmp = copy.copy(assesment)
    asses_tmp = sorted(asses_tmp, reverse=True)
    r_li = []
    for r in range(len(li)):
        r_li.append(li[assesment.index(asses_tmp[r])])
    end_li = []
    for e in r_li: 
        if len(end_li) >= 10:
            break
        if e not in end_li:
            end_li.append(e)
    return end_li

while True:
    inp = search_max(li)
    print('最適解')
    print(inp)
    t = input("入力してください: ")
    print("場所共に一致している:2, 含まれる:1, 含まれない:0 を選択")
    ans = list(map(int, input().split()))
    bit = ans
    if sum(ans) == 10:
        exit()
    for i in range(5):
        if ans[i] == 0:
            tmp = [item for item in li if t[i] not in item]
            li = tmp
        elif ans[i] == 1:
            tmp = [item for item in li if (t[i] in item) and (t[i] != item[i])]
            li = tmp
        else:
            tmp = [item for item in li if t[i] == item[i]]
            li = tmp
    print(li)
    print(len(li))
    
    

