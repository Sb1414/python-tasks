def get_balance(name, transactions) -> int:
    res = 0
    money = {i['name']: i['amount'] for i in transactions}
    if name in money:
        res = money[name]
    return res

def count_debts(names, amount, transactions) -> dict:
    res = {i : amount - get_balance(i, transactions) for i in names if amount > get_balance(i, transactions)}
    return res