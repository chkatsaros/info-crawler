import json
import xmltodict

# XML to JSON conversion

def eh_converter(input, output):
    xml_file = open(input) 
    data_dict = xmltodict.parse(xml_file.read())
        
    json_data = json.dumps(data_dict)

    json_file = open(f'{output}.json', "w") 
    json_file.write(json_data)
    json_file.close()