'''
Ex– Number is 54
it is divisible by own sum (5+4) of its digit 9
Some other harshad number are 21, 156,54,120 et
'''


n=input()
k=[int(i) for i in n]
k=sum(k)
if(int(n) % k==0):
    print("Harshad num")
else:print("not Harshad  num")
