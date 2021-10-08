str1 = input()
for i in str1.split():
    str1 = str1.replace(i, i.capitalize())
print(str1)
