arr = [x for x in input("Enter array:").split()]
ind = int(input("Enter index:"))
ad = input("Enter element to add:")
arr.insert(ind-1, ad)
print(*arr)




# 2 6 8 10
# 2
# 4
# 2 4 6 8 10
