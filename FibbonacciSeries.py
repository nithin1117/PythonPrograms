#fibbonacci
a =[0,1]
n = int(input("Fibbonacci sequence Range upto: "))
for i in range(2,n):
    a.append(a[-1] + a[-2])
print(*a)

# output
# Fibbonacci sequence Range upto: 10
# 0 1 1 2 3 5 8 13 21 34
