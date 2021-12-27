import json

def load(file_path):
    with open(f"defines/{file_path}.json") as f:
        return json.load(f)

defaults = load("defaults")
text = load("text")
