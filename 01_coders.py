import json

def getData(filename) :
    with open (filename, "r") as f :
        data = json.load(f)
    return data

def displayUsers(data):
    print("users and their connections -\n")

    id_to_name = {player['id']: player['name'] for player in data['players']}
    id_to_club = {club['id']: club['name'] for club in data['clubs']}
    
    for user in data['players'] :
        teammate_names = [id_to_name[t] for t in user['teammates']]
        liked_club_names = [id_to_club[c] for c in user['liked_clubs']]
        print(f"ID: {user['id']} - {user['name']} is teammates w/ : {teammate_names} and liked clubs are {liked_club_names}")

    print("\npages info -\n")

    for page in data['clubs'] :
        print(f"{page['id']}: {page['name']}")

data = getData("01_football_dataset.json")

data = displayUsers(data)