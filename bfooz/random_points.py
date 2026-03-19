import random
import matplotlib.pyplot as plt

def draw_random_points(n):
    x = [random.random() for _ in range(n)]
    y = [random.random() for _ in range(n)]
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, color='red', s=30, alpha=0.6)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{n} puntos aleatorios en el cuadrado [0,1] × [0,1]')
    plt.grid(True, alpha=0.3)
    plt.gca().set_aspect('equal')
    plt.show()
