string = input().split()
substring = input()

lowerSubstr = substring.lower()
for word in string:
    if lowerSubstr in word.lower():
        print(word)