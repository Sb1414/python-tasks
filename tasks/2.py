num = 0
count = 0
integer = 0

while integer != '': 
    integer = input()
    try:
        if int(integer) % 2 == 0:
            num += int(integer)
            count+=1
    except ValueError:
        pass

if count == 0:
    print(0)
else:
    print(num)