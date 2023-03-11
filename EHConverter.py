import json
import csv
import xmltodict

# XML to JSON conversion

xml_file = open("example.xml") 
data_dict = xmltodict.parse(xml_file.read())
    
json_data = json.dumps(data_dict)

json_file = open("example.json", "w") 
json_file.write(json_data)
json_file.close()

# JSON to CSV conversion
json_file = open("example.json" )
data = json.load(json_file)
 
eh_data = data['EmailHarvester']
 
# now we will open a file for writing
csv_file = open('example.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(csv_file)

# Writing headers of CSV file
header = 'email'
csv_writer.writerow([header])

for email in eh_data['email']:
    # Writing data of CSV file
    csv_writer.writerow([email])
 
xml_file.close()
json_file.close()
csv_file.close()