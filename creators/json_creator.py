import json
from pathlib import Path

def json_creator(title, path):
    th_json = open('./temp/harvester.json')
    eh_json = open('./temp/emailharvester.json')
    am_json = open('./temp/amass.json')
    
    th_data = json.load(th_json)
    eh_data = json.load(eh_json)
    am_data = json.load(am_json) 

    result = {
        "TheHarvester": th_data["TheHarvester"],
        "EmailHarvester": eh_data["EmailHarvester"],
        "Amass": am_data["Amass"]
    }
    
    output_path = Path(path).joinpath(f'{title}.json')
    output_file = output_path.open("w") 
    output_file.write(json.dumps(result))
    
    th_json.close()
    eh_json.close()
    am_json.close()
    output_file.close()