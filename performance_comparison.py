import random
import time
from linear_search import linear_search
from binary_search import binary_search
import matplotlib.pyplot as plt

# Функция для измерения времени выполнения
def measure_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    end_time = time.time()
    return end_time - start_time

# Измерение времени для разных размеров списков
sizes = [10, 100, 1000, 10000]
linear_times = []
binary_times = []

for size in sizes:
    arr = sorted(random.sample(range(1, size * 10), size))
    target = random.choice(arr)

    # Линейный поиск
    linear_time = measure_time(linear_search, arr, target)
    linear_times.append(linear_time)

    # Бинарный поиск
    binary_time = measure_time(binary_search, arr, target)
    binary_times.append(binary_time)

# Построение графика
plt.plot(sizes, linear_times, label="Линейный поиск", marker='o')
plt.plot(sizes, binary_times, label="Бинарный поиск", marker='x')
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение времени выполнения поиска")
plt.legend()
plt.grid(True)
plt.savefig("performance_comparison_graph.png")  # Сохранение графика в файл
plt.show()