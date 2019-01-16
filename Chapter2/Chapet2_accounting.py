import json

filename = 'skychallenge_accounting_input.txt'

my_list = []

def extract_dict(v):
    if isinstance(v, dict):                 #if value is a dict
        for k, v2 in v.items():
            extract_dict(v2)                #check next element
    elif isinstance(v, list):               #if value is a list
        for i, v2 in enumerate(v):
            extract_dict(v2)                #check next element
    else:                                   #if value is just a single type value (int, string, etc.)
        if type(v) == int:                  #check type of value
            my_list.append(v)

with open(filename) as f:
    dicti = json.load(f)

extract_dict(dicti)

result = sum(my_list)
print(result)
