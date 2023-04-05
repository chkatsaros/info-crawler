import dicttoxml
import json
from pathlib import Path

def xml_creator(title, path):
    json_path = Path(path).joinpath(f'{title}.json')
    json_file = open(json_path)
    
    data = json.load(json_file)
    xml_data = dicttoxml.dicttoxml(data, custom_root='InfoCrawler', attr_type=False, return_bytes=False)
    
    output_path = Path(path).joinpath(f'{title}.xml')
    output_file = output_path.open("w")
    output_file.write(xml_data)
    
    json_file.close()
    output_file.close()