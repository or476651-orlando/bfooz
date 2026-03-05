from bfooz import knapsack_boolean, knapsack

def test_knapsack():
    w = [2, 1, 3, 2]
    p = [3, 2, 4, 2]
    capacity = 5
    goal = 7
    assert knapsack_boolean.knapsack_boolean(goal, capacity, p, w) == True