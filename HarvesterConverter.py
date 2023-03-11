import json

json_file = open('example.json')
data = json.load(json_file)

harvester_dict = {'TheHarvester': data}

print(harvester_dict)

json_file.close()