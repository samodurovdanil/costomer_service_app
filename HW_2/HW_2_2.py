import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "товар": item,
        "количество": quantity,
        "цена": price,
        "покупатель": buyer,
        "дата": date
    }
    with open('orders.json', 'r+', encoding='utf-8') as f_n:
        objs = json.load(f_n)
        objs['orders'].append(dict_to_json)
        f_n.seek(0)
        f_n.write(json.dumps(objs, sort_keys=True, indent=4))


write_order_to_json('item', 'quantity', 'price', 'buyer', 'date')
