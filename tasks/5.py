a = []

for i in range(5):
    a.append(int(input()))

a.sort(reverse = True)

for i in range(5):
    print(a[i])