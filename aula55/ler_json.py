import json

with open('arquivo.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for key, values in v.items():
        print(f'{key}: {values}')
    print()
