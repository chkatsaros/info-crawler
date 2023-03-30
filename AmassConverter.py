import json

json_file = open('example.json')

data = []

for line in json_file:
    line_dict = json.loads(line)
    data.append(line_dict)

amass_dict = {'Amass': data}
