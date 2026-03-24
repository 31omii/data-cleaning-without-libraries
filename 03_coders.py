import json

def load_data(filename):
    with open(filename, "r") as f :
        return json.load(f)

def find_people_u_may_know(user_id, data) :
    user_teammates = {}
    for user in data['players'] :
        user_teammates[user['id']] = set(user['teammates'])

    if user_id not in user_teammates :
        print("your are lonely!")

    direct_teammates = user_teammates[user_id]
    suggestions = {}

    for friend in direct_teammates :
        for mutual in user_teammates[friend] :
            if mutual != user_id and mutual not in direct_teammates : 
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    sorted_suggestions = sorted(suggestions.items(), key = lambda x: x[1], reverse = True)
    return [user_id for user_id, _ in sorted_suggestions]

data = load_data("01_football_dataset.json")

id_to_name = {player['id']: player['name'] for player in data['players']}

user_id = int(input("Enter player ID to get suggestions: "))

recc = find_people_u_may_know(user_id, data)

print(f"\nPeople You May Know for {recc} : ")

recc_names = [id_to_name[r] for r in recc]

print(f"\nPeople You May Know for {id_to_name.get(user_id, 'Unknown')} : ")
print(recc_names)