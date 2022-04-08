import pandas as pd

li = []
with open("/Users/natsumi/Documents/wordle/goi.csv", "r", encoding="Shift JIS") as f:
    file_data = f.readlines()
    for i in file_data:
        tmp = i.split(',')
        if len(tmp[2]) == 5:
            li.append(tmp[2])

with open("/Users/natsumi/Documents/wordle/dict.csv", "w") as f:
    for i in range(len(li)):
        f.write(li[i]+'\n')
