#check the number is prime or not 
def prime():
    n = int(input("enter number to check prime: "))
    pri = False
    if n>1:
        for i in range(2,n):
            if n%2==0:
                pri = True
                break
        if pri:
            print('not prime')
        else:
            print("{} is prime".format(n))
    else:
        print("enter positive numb: ")
        prime()
prime()

# output
# enter number to check prime: -10
# enter positive numb
# enter number to check prime: 5
# 5 is prim
