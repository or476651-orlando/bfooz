from bfooz import knapsack_boolean, knapsack

def test_knapsack():
    assert knapsack_boolean(10, 10, [1,2,1,3], [1,2,3,4]) == False
    assert knapsack_boolean(6, 4, [1,2,3], [1,2,3]) == False
    assert knapsack_boolean(7, 5, [3, 2, 4, 2], [2, 1, 3, 2]) == True