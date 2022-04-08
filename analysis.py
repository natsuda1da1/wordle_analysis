li = []

with open("/Users/natsumi/Documents/wordle/dict.csv", "r", encoding="utf-8") as f:
    file_data = f.readlines()
    for i in file_data:
        li.append(i.split('\n')[0])

while True:
    t = input("入力してください: ")
    print("場所共に一致している:2, 含まれる:1, 含まれない:0 を選択")
    ans = list(map(int, input().split()))
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
    if sum(ans) == 5:
        exit
    

