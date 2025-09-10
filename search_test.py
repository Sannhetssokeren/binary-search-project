import random
from binary_search import binary_search

random_list = sorted(random.sample(range(1, 1000), 100))

test_values = [random.choice(random_list), 9999]
results = {}

for value in test_values:
    index = binary_search(random_list, value)
    results[value] = index

with open("binary_search_results.txt", "w") as file:
    for value, index in results.items():
        file.write(f"Значение {value}: Индекс {index}\n")