n = int(input())
n1 = n**2
n = str(n)
n1 = str(n1)
if (n == n1[-len(n):]):
    print("Automorphic")
else:
    print("non-automorphic")
    
    
'''eg 5 input na 25**2 = 625 and 625 last digit is 25
