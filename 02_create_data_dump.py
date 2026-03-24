import json
import random

with open("01_football_dataset.json", "r") as f:
    data = json.load(f)

players = data["players"]

for player in players:
    
    if random.random() < 1:
        anomaly_type = random.choice(["name", "teammates", "followed_clubs"])
        
        if anomaly_type == "name":
            player["name"] = None
        
        elif anomaly_type == "teammates":
            player["teammates"] = []
        
        elif anomaly_type == "followed_clubs":
            player["followed_clubs"] = None

with open("02_football_data_dump.json", "w") as f:
    json.dump(data, f, indent=4)

print("Dataset with anomalies created!")