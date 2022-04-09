li = []

with open("./dict.csv", "r", encoding="utf-8") as f:
    file_data = f.readlines()
    for i in file_data:
        li.append(i.split('\n')[0])