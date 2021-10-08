arr = [int(x) for x in input("Enter array to print runner score:").split()]
arr = list(set(arr))
arr.sort(reverse =True)
print(arr[1])
