import csv
import json

def readCsvWriteJson():
    filterdata = []
     
     
    with open('MOCK_DATA.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            if 'ip_address' in row:
                del row['ip_address']
                
            if row.get('gender') == 'Female':
                filterdata.append(row)
                
    with open('output.json', 'w') as json_file:
        json.dump(filterdata, json_file, indent=4)
        
    return filterdata

print(readCsvWriteJson())