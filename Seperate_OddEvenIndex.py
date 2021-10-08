arr = [1,2,3,4,5,6]

odd_ind = [arr[i] for i in range(len(arr)) if i%2==0]
print(odd_ind)

even_ind = [arr[i] for i in range(len(arr)) if i%2!=0]
print(even_ind)


# output
# [1, 3, 5]
# [2, 4, 6]
