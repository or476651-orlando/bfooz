import networkx as nx
import random
import itertools

def generated_graph(n):
  g = nx.Graph()
  g.add_nodes_from(range(n))
  edges = list(itertools.combinations(range(n),2))
  weighted_edges = []
  for edge in edges:
    edge = list(edge)
    edge.append(random.randint(1,10))
    weighted_edges.append(edge)
  g.add_weighted_edges_from(weighted_edges)
  return g

def solve_spanning_tree(n):
  G = generated_graph(n)
  tree = nx.minimum_spanning_tree(G)
  position=nx.spring_layout(tree)
  weight_labels = nx.get_edge_attributes(tree, 'weight')
  nx.draw_networkx_edge_labels(tree, pos=position,
                             edge_labels=weight_labels,
                             font_color='red')
  nx.draw(tree, with_labels="True", pos=position)
  return tree
