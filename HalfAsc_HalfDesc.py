arr=[int(x) for x in input().split()]
n=len(arr)
half=n//2

arr.sort()
x=arr[:half]

arr.reverse()
y=arr[:half]
print(*x+y)
