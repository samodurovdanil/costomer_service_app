import yaml

content = {
    'item_1': ['list'],
    'item_2': 2,
    'item_': {
        'key_1': '2€',
        'key_2': '2€'
    }
}

with open('file.yaml', 'r+', encoding='utf-8') as f:
    yaml.dump(content, f, default_flow_style=False, allow_unicode=True)
    f.seek(0)
    print(f.read())
