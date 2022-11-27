import json
import re

with open("input.txt") as file:
    content = [i.split()[0] for i in file.readlines() if len(i.strip()) > 0]

def get_popular_name_from_file(filename):
    uniq = {}
    for i in filename:
        uniq[i] = uniq.get(i, 0) + 1
    cnt_max = max(uniq.values())
    res = sorted([i[0] for i in uniq.items() if i[1] == cnt_max])
    return(', '.join(res))

print(get_popular_name_from_file(content))