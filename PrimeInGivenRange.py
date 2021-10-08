print("enter range:")
n1 = int(input())
n2 = int(input())
pri = []
for i in range(n1,n2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        pri.append(i)
print(pri)
