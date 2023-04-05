import json
import dicttoxml

def am_converter(input, output):
    json_file = open(input)

    data = []

    for line in json_file:
        line_dict = json.loads(line)
        data.append(line_dict)

    amass_dict = { 'Amass': data }
    
    # Convert amass json output
    json_file = open(f'{output}.json', "w") 
    json_file.write(json.dumps(amass_dict))
    json_file.close()
    
    # Create amass xml output
    xml_data = dicttoxml.dicttoxml(amass_dict['Amass'], custom_root='Amass', attr_type=False, return_bytes=False)
    xml_file = open(f'{output}.xml', "w")
    xml_file.write(xml_data)
    xml_file.close()
