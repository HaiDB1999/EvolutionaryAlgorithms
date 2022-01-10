from func import *
from gene import *
import json

if __name__ == '__main__':
  f = open("../data/ga-dem1_r25_1_0.json")
  data = json.load(f)
  f.close()

  num_of_relays = data['num_of_relays']
  num_of_sensors = data['num_of_sensors']

  relays = data['relays']
  sensors = data['sensors']
  center = data['center']
  radius = data['radius']

  list_node = [center] + relays + sensors
  nodes = []
  for i in range(len(list_node)):
    nodes.append([i, list_node[i]['x'], list_node[i]['y'], list_node[i]['z']])