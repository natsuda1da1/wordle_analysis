import copy
import random

from numpy import average
from tqdm import tqdm

li = []
bit = [0,0,0,0,0]
rate = []

with open("./A_data_new.csv", "r", encoding="utf-8") as f:
    file_data = f.readlines()
    for i in file_data:
        li.append(i.split('\n')[0])

tmp_li = copy.deepcopy(li)
tmp2_li = copy.deepcopy(li)

def search_max(li):
    best = [[] for _ in range(5)]#それぞれ何回出現するか
    ans = [[] for _ in range(5)]#順位
    moji = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモラリルレロヤユヨワヲンガギグゲゴザジズヅゼゾダジヂヅデドバビブヴベボパピプペポァィゥェォッャュョヮー'
    #moji = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもらりるれろやゆよわをんがぎぐげござじずぜぞだじぢづでどばびぶヴべぼぱぴぷぺぽぁぃぅぇぉっゃゅょゎー'
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
    #sum_beet = [sum(best[i]) for i in range(5)]
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
            return li[0]

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
    return end_li[random.randint(0, 3)]

rand_list = [random.choice(li) for _ in range(100)]
cntter = 0
pbar =  tqdm(range(len(rand_list)))
for i in pbar:
    pbar.set_postfix_str(average(rate))
    cnt = 0
    t = rand_list[i]
    ans = [0, 0, 0, 0, 0]
    li = tmp2_li
    while True:
        if len(li) == 1:
            inp = li[0]
            cnt += 1
            rate.append(cnt)
            break
        else:
            inp = search_max(li)
        if t == inp:
            rate.append(cnt)
            break
        for i in range(5):
            if inp[i] in t:
                if inp[i] == t[i]:
                    ans[i] = 2
                else:
                    ans[i] = 1
            else:
                ans[i] = 0
        bit = ans
        if sum(ans) == 10:
            exit()
        for i in range(5):
            if ans[i] == 0:
                tmp = [item for item in li if inp[i] not in item]
                li = tmp
            elif ans[i] == 1:
                tmp = [item for item in li if (inp[i] in item) and (inp[i] != item[i])]
                li = tmp
            else:
                tmp = [item for item in li if inp[i] == item[i]]
                li = tmp
        cnt += 1
        #print(li)
        #print(len(li))

print('正解までの平均回数は{}回です'.format(average(rate)))