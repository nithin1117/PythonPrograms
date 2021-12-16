n = 18
a = 0
for i in range(n):
    if i>0:
        if n%i==0:
            a += i

if a>n:
    print("Abundant number")
else:
    print("Not an abundant number")
