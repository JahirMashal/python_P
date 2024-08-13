# import requests

# def getMyIp():

#     response = requests.get('https://api.ipify.org/?format=json')
    

#     if response.status_code == 200:
#         data = response.json()
 
#         return data.get('ip')
#     else:
#         return "Failed to retrieve IP"


# print(getMyIp())

import requests

def getMyIp():
    
    response = requests.get('https://api.ipify.org/?format=json')
    
    if response.status_code == 200:
        data = response.json()
        
        return data.get('ip')
    
    else:
        return "Failed to retrieve IP"
    

print(getMyIp())