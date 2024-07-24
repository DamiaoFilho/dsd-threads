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


array = []
for i in range(lenght):
    array.append(random.randint(1, 99))


start_time = time.time()
result = calculate_with_threads(array, threads)
end_time = time.time()

print(f"Threads\n{result}\nSeconds:{end_time-start_time}")

start_time = time.time()
normal_sum = 0
for i in array:
    normal_sum += i
end_time = time.time()

print(f"Normal\n{normal_sum}\nSeconds:{end_time-start_time}")

start_time = time.time()
result = sum(array)
end_time = time.time()

print(f"Sum\n{result}\nSeconds:{end_time-start_time}")
