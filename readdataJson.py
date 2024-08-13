import json

def readJson():
    
    with open('MOCK_DATA.json', 'r') as file:
        data = json.load(file)
    

    filtered_data = [record for record in data if record['gender'] == 'Male']
    

    for record in filtered_data:
        record['Full_name']= f"{record['First_name']} {record['Last_name']}"
    
    return filtered_data


print(readJson())