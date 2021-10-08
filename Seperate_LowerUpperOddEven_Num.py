a = "String1234"
lower_a = []
upper_a = []
digit = []
for i in a:
    if i.isalpha() and i.islower():
        lower_a.append(i)
    if i.isalpha() and i.isupper():
        upper_a.append(i)
    if i.isnumeric():
        digit.append(i)
odd= [x for x in digit if int(x)%2!=0]
even= [x for x in digit if int(x)%2==0]
print(*lower_a,*upper_a,*odd,*even,sep="")
