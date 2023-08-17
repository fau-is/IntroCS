import json

def load_data():
    with open('../tests/ressources/followers.json', 'r') as file:
        data = json.load(file)
    return data["followers"]



print(load_data())