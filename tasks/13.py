import json

def mean_age(json_string):
    st = json.loads(json_string)
    age = sum(i.get('age') for i in st)
    mean = age / len(st)
    res = "{" + "\"mean_age\": " + str(mean) + "}"
    return res

with open('input.txt') as file:
    content = file.read()

print(mean_age(content))