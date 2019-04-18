import json
from pprint import pprint

INPUT_FILE = "/home/aero/UAVClassifier/testjson/bruteparsed.json"

data = json.load(INPUT_FILE)
# data = INPUT_FILE:# WARNING:

print(data)
