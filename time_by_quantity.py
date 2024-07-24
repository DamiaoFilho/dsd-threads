import random
import concurrent.futures
import time
import matplotlib.pyplot as plt
from functions import calculate_with_threads

print("Threads Quantity")
threads = int(input())


lenghts = [100, 5000, 750000, 1000000, 57000000, 500000000, 1000000000]


times_threads = []
times_normal = []
times_sum = []



for l in lenghts:

    array = [random.randint(0,99)] * l     

    start_time = time.time()
    result = calculate_with_threads(array, threads)
    end_time = time.time()

    times_threads.append(end_time-start_time)

    start_normal_time = time.time()
    normal_sum = 0
    for i in array:
        normal_sum += i
    end_normal_time = time.time()

    times_normal.append(end_normal_time-start_normal_time)

    start_sum_time = time.time()
    result = sum(array)
    end_sum_time = time.time()

    times_sum.append(end_sum_time-start_sum_time)

    print(len(array))

plt.figure(figsize=(5, 5))
plt.plot(lenghts, times_threads, label='Threads')
plt.plot(lenghts, times_normal, label='Normal')
plt.plot(lenghts, times_sum, label='Sum')
plt.xlabel('Vector Lenght')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time by Vector Lenght ')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()