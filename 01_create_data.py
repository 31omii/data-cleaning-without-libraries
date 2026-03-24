import json
import random

base_players = [
("Cristiano Ronaldo",201),
("Lionel Messi",202),
("Neymar Jr",203),
("Zlatan Ibrahimovic",204),
("Kylian Mbappe",205),
("Mohamed Salah",206),
("Harry Kane",207),
("Robert Lewandowski",208),
("Eden Hazard",209),
("Erling Haaland",210)
]

clubs = [
{"id":201,"name":"Real Madrid"},
{"id":202,"name":"FC Barcelona"},
{"id":203,"name":"Santos"},
{"id":204,"name":"AC Milan"},
{"id":205,"name":"Paris Saint Germain"},
{"id":206,"name":"Liverpool"},
{"id":207,"name":"Bayern Munich"},
{"id":208,"name":"Borussia Dortmund"},
{"id":209,"name":"Chelsea"},
{"id":210,"name":"Manchester City"}
]

players = []
id_counter = 1

for i in range(7): 
    for name,club in base_players:

        players.append({
            "id": id_counter,
            "name": f"{name}_{i+1}",
            "teammates": [],
            "liked_clubs": [club]
        })

        id_counter += 1

player_ids = [p["id"] for p in players]

for p in players:
    possible = [x for x in player_ids if x != p["id"]]

    teammates = random.sample(possible, random.randint(2,5))

    p["teammates"] = teammates


data = {
"players": players,
"clubs": clubs
}

with open("01_football_dataset.json","w") as f:
    json.dump(data,f,indent=4)

print("Dataset created with teammates!")