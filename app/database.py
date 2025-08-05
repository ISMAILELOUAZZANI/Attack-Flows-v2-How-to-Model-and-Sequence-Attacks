import json
import os

DATA_DIR = "attack_flows_db"
os.makedirs(DATA_DIR, exist_ok=True)

def save_flow(flow):
    path = os.path.join(DATA_DIR, f"{flow.id}.json")
    with open(path, "w") as f:
        f.write(flow.json())

def load_flow(flow_id):
    path = os.path.join(DATA_DIR, f"{flow_id}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)