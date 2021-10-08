arr = [12, 23, 4, 6, 7]
n = len(arr)

if n % 2 == 0:
    pass
else:
    n = n-1

for i in range(0, n, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)
