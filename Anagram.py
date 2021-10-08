n = input().casefold()
s = input().casefold()
def anagram(n, s):
    for i in n:
        if i in s:
            return "Yes"
    return "No"
print(anagram(n, s))

# ABCDEFG
# efcd
# Yes
