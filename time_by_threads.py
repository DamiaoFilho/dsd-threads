import random
import concurrent.futures
import time
import matplotlib.pyplot as plt
import numpy as np
from functions import calculate_with_threads

print("Threads Quantity")
threads = int(input())


print("Array Length")
lenght = int(input())



times = []

array = []
for i in range(lenght):
    array.append(random.randint(1, 99))

for nt in range(1, threads+1):
    start_time = time.time()
    result = calculate_with_threads(array, nt)
    end_time = time.time()

    times.append(end_time-start_time)

print(times)
plt.figure(figsize=(12, 8))
plt.plot([i for i in range(1, threads+1)], times, marker='o', label='Normal Loop')
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Number of Threads')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time by Number of Threads')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()