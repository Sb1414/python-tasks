string = input()

newString = ' '.join(string.split())
newString = newString.replace(' ', '*')

print(newString)