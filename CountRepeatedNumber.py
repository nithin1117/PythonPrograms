arr = [12, 13, 24, 12, 12, 13]
dict1 = list(dict.fromkeys(arr))
for i in dict1:
    print(f"{i} is repeated {arr.count(i)} time\'s and found in index {arr.index(i)}")
