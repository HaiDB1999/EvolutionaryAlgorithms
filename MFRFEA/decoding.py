# Tao ma tran cac canh
def matrix_edge_adjacents(G):
  """
    return {
      'node': [node1, node2, ...],,
      ....
    }
  """
  V1, E1 = G
  result = {}
  for node in V1:
    adjacents = []
    for edge in E1:
      if(edge[0] == node):
        adjacents.append(edge[1])
      if(edge[1] == node):
        adjacents.append(edge[0])
    result[node] = adjacents
  return result

def check_cycle():
  pass

def decoding_network(G, relays, sensors, r, indiv_name):
  """
    G(V, E): V: array relay, sensor node, E array edges [(a,b),..]
    relays: arrry relays node
    sensors: arrry sensor node
    r: number relay selected (r <= n_relay)
    indiv_name: hoán vị của sensors, relays
  """
  (V, E) = G
  m, n = len(relays), len(sensors)

  V_t = [0] # 0 is node source
  E_t = []
  relays.sort(key=lambda x: indiv_name.index(x))
  for rn in relays[:r]:
    V_t.append(rn)
    E_t.append((0, rn))

  V_t += sensors
  sensors.sort(key=lambda x: indiv_name.index(x))
  for s in sensors:
    adj = ADJACENTS[s]
    adj.sort(key=lambda x: indiv_name.index(x))
    for u in adj:
      if (u in V_t) and (check_cycle((u, s), (V_t, E_t)) == False):
        E_t.append((u,s))
        break

  if(len(E_t) < len(sensors)+r):
    return ([0], [])
  return (V_t, E_t)