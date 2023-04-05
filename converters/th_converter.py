import json

def th_converter(input, output):
    json_file = open(input)
    data = json.load(json_file)

    harvester_dict = {'TheHarvester': data}

    output_file = open(f'{output}.json', "w") 
    output_file.write(json.dumps(harvester_dict))

    json_file.close()
    output_file.close()