arr = ["nitin", "malayalam", "mom", "nithin"]
ar = [i for i in arr if i[::] == i[::-1]]

cnt = arr[0]
for j in ar:
    if len(j) > len(cnt):
        cnt = j
print(cnt)
print(len(cnt))
