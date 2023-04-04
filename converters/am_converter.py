import json

def am_converter(input, output):
    json_file = open(input)

    data = []

    for line in json_file:
        line_dict = json.loads(line)
        data.append(line_dict)

    amass_dict = {'Amass': data}
    
    json_file = open(output, "w") 
    json_file.write(json.dumps(amass_dict))
    json_file.close()
