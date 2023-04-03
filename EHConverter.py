import json
import xmltodict

# XML to JSON conversion

xml_file = open("example.xml") 
data_dict = xmltodict.parse(xml_file.read())
    
json_data = json.dumps(data_dict)

json_file = open("example.json", "w") 
json_file.write(json_data)
json_file.close()