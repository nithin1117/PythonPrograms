arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 9 ]
k = len(arr)
n = k
if k%2!=0:
    n = k-1
else:
    pass

sum1 = 0
for i in range(0, n, 2):
    v = arr[i+1]-arr[i]
    sum1 += v

for j in range(1, k-1, 2):
    v = arr[j+1]-arr[j]
    sum1 += v
print(sum1)



