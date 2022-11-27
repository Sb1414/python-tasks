count = 0

slovo = input().split(", ")
copy = ["a", "b", "c"]
number = [0, 0, 0]
flag = True
for i in range(0, len(slovo)):
    count = 1
    j = 0
    for k in range(i + 1, len(slovo)):
        if slovo[i] == slovo[k]:
            count += 1
    if copy[j] != slovo[i]:
        if number[j] < count:
            copy[j + 2] = copy[j + 1]
            copy[j + 1] = copy[j]
            copy[j] = slovo[i]
            number[j+2] = number[j+1]
            number[j+1] = number[j]
            number[j] = count
        elif number[j+1] < count and copy[j] != slovo[i]:
            copy[j + 2] = copy[j + 1]
            copy[j + 1] = slovo[i]
            number[j+2] = number[j+1]
            number[j+1] = count
        elif number[j+2] < count and copy[j + 1] != slovo[i]:
            copy[j+2] = slovo[i]
            number[j+2] = count

for i in range(0, 3):
    if number[i] != 0:
        print(copy[i], ": ", number[i], sep="", end="\n")

# другой вариант:

# in_string = list(map(str, input().split(', ')))
# dict = {}
# for key in in_string:
#     dict[key] = dict.get(key, 0) + 1
# from operator import itemgetter    
# sorted_keys = sorted(dict.items(), key=itemgetter(1), reverse=True)[:3]
# for key, val in sorted_keys:
#     print('%s: %s' % (key, val))