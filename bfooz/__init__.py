import itertools
import networkx as nx

def hello():
    return "Hello, world!"

def is_proper_coloring(graph, coloring):
  for edge in graph.edges():
    if coloring[edge[0]] == coloring[edge[1]]:
      return False
  return True

def is_3_colorable(graph):
  n = graph.order()
  colorings = itertools.product([0,1,2], repeat = n)
  for coloring in colorings:
    if is_proper_coloring(graph, coloring):
      return coloring
  return False

def is_hamiltonian_cycle(graph,cycle):
  """ Checks if cycle is a hamiltonian cycle in graph """
  n = len(set(cycle))
  if n != graph.order():
    return False
  for i in range(n-1):
    if not graph.has_edge(cycle[i],cycle[i+1]):
      return False
  if not graph.has_edge(cycle[n-1],cycle[0]):
    return False
  return True

def is_hamiltonian(graph):
  vertices = list(graph.nodes())
  if len(vertices) < 3:
    return False
  perms = itertools.permutations(vertices)
  for perm in perms:
    if is_hamiltonian_cycle(graph,perm):
      return perm
  return False 

def knapsack(desired_value, knapsack_capacity, profits, weights):
  combs = itertools.product([0,1], repeat = len(profits))
  combinaciones = list(combs)
  for combinacion in combinaciones:
    check_weight = sum([combinacion[i] * weights[i] for i in range(len(combinacion))])
    if check_weight <= knapsack_capacity:
      check_value = sum([combinacion[i] * profits[i] for i in range(len(combinacion))])
      if check_value >= desired_value:
        print('Si hay solución. Una de ellas es la que la tupla a continuación codifique: ')
        return combinacion
  print('No hay solución')
  return None
