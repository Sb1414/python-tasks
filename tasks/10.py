def lists_sum (*args, unique=False):
    arr = []
    for i in args:
        arr = [*arr, *i]
    if (unique):
        arr = set(arr)
    return sum(arr)