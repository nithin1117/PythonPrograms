arr = [11, 22, 4, 5, 10, 3, 2, 8, 9]
max1 = arr[0]
for i in range(len(arr)-1):
    if max1 < arr[i+1]:
        max1 = arr[i+1]
print(max1)


# (or)


arr.sort(reverse=True)
print(arr[0])

# or


print(max(arr))
