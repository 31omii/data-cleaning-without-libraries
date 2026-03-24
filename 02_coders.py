import json

def cleanData(data) :

    data['players'] = [user for user in data['players'] if user['name'.strip()]]
    
    for user in data['players'] :
        user['teammates'] = list(set(user['teammates']))
    
    data['players'] = [user for user in data['players'] if user['teammates'] or user['liked_clubs']]

    unqclubs = {}
    for page in data['clubs'] :
        unqclubs[page['id']] = page
    data['clubs'] = list(unqclubs.values())

    return data

data = json.load(open("02_football_data_dump.json"))
data = cleanData(data)
json.dump(data, open('02_football_dataset_clean', 'w'), indent = 4)
print("data has been cleaned!!!")