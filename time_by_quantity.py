import random
import concurrent.futures
import time
import matplotlib.pyplot as plt
from functions import calculate_with_threads

print("Threads Quantity")
threads = int(input())


lenghts = [100, 5000, 750000, 1000000, 57000000]


times_threads = []
times_normal = []
times_sum = []



for l in lenghts:

    array = []
    for i in range(l):
        array.append(random.randint(1, 99))


    start_time = time.time()
    result = calculate_with_threads(array, threads)
    end_time = time.time()

    times_threads.append(end_time-start_time)

    start_time = time.time()
    normal_sum = 0
    for i in array:
        normal_sum += i
    end_time = time.time()

    times_normal.append(end_time-start_time)

    start_time = time.time()
    normal_sum = 0
    for i in array:
        normal_sum += i
    end_time = time.time()

    times_sum.append(end_time-start_time)

plt.figure(figsize=(12, 8))
plt.plot(lenghts, times_threads, label='Threads')
plt.plot(lenghts, times_normal, label='Normal')
plt.plot(lenghts, times_sum, label='Sum')
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Vector Lenght')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time by Vector Lenght ')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()