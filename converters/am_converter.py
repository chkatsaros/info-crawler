import json

def am_converter(input, output):
    json_file = open(input)

    amass_dict = { 'Amass': {} }

    for line in json_file:
        line_dict = json.loads(line)
        name = line_dict['name']
        del line_dict['name']
        amass_dict['Amass'][name] = line_dict
    
    json_file = open(f'{output}.json', "w") 
    json_file.write(json.dumps(amass_dict))
    json_file.close()
