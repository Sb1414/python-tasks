str_1 = input().split(", ")
sting = ""
new_li = [x.lower() for x in str_1]
my_set = set(new_li)
sorted_set = sorted(my_set)
for x in sorted_set:
    sting += x + ", "

string = str(sting)
index = len(string)
s = string[:index-2]
print(s)