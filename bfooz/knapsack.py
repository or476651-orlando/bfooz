import itertools

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

def knapsack_boolean(desired_value, knapsack_capacity, profits, weights):
  combs = itertools.product([0,1], repeat = len(profits))
  combinaciones = list(combs)
  for combinacion in combinaciones:
    check_weight = sum([combinacion[i] * weights[i] for i in range(len(combinacion))])
    if check_weight <= knapsack_capacity:
      check_value = sum([combinacion[i] * profits[i] for i in range(len(combinacion))])
      if check_value >= desired_value:
        print('Si hay solución. Una de ellas es la que la tupla a continuación codifique: ')
        return True
  print('No hay solución')
  return False