import random
import concurrent.futures
import time
import math


print("Threads Quantity")
threads = int(input())

print("Array Length")
lenght = int(input())

array = []
for i in range(lenght):
    array.append(random.randint(1, 99))

#Normal
start_time = time.time()
normal_sum = 0
for i in array:
    normal_sum += i
end_time = time.time()
    
print(f"Normal\n{normal_sum}\nSeconds:{end_time-start_time}")


#Threads
def createThread(start, end, iterable):
    result = 0
    for i in range(start, end):
        result += iterable[i]
    return result


def sum_with_threads(threads, array):
    elements_per_thread = int(len(array)/threads)
    if elements_per_thread == 0:
        elements_per_thread = 1 

    threads_sum = []
    actual_index = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []

        for i in range(threads):
                futures.append(
                    executor.submit(createThread, actual_index, actual_index+elements_per_thread, array)
                )

                #if the number of threads is greater than the array length
                if actual_index == len(array)-1:
                    actual_index += elements_per_thread
                    break

                actual_index += elements_per_thread
            
        while actual_index < len(array)-1:

            elements_per_thread = int((actual_index - len(array))/threads)     
            if elements_per_thread == 0:
                elements_per_thread = 1 

            for i in range(threads):
                futures.append(
                    executor.submit(createThread, actual_index, actual_index+elements_per_thread, array)
                )
                if actual_index == len(array)-1:
                    break
                actual_index += elements_per_thread


        for future in concurrent.futures.as_completed(futures):
            threads_sum.append(future.result())
    
    threads_result = 0
    for i in threads_sum:
        threads_result += i

    return threads_result


start_time = time.time()

elements_per_thread = int(lenght/threads)
if elements_per_thread == 0:
    elements_per_thread = 1 

threads_sum = []
actual_index = 0

with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    futures = []

    for i in range(threads):
            futures.append(
                executor.submit(createThread, actual_index, actual_index+elements_per_thread, array)
            )

            #if the number of threads is greater than the array length
            if actual_index == len(array)-1:
                print("entrou")
                actual_index += elements_per_thread
                break

            actual_index += elements_per_thread
        
    while actual_index < len(array)-1:

        elements_per_thread = int((actual_index - len(array))/threads)     
        if elements_per_thread == 0:
            elements_per_thread = 1 

        for i in range(threads):
            futures.append(
                executor.submit(createThread, actual_index, actual_index+elements_per_thread, array)
            )
            if actual_index == len(array)-1:
                break
            actual_index += elements_per_thread


    for future in concurrent.futures.as_completed(futures):
        threads_sum.append(future.result())
        

threads_result = 0
for i in threads_sum:
    threads_result += i
end_time = time.time()

print(f"Threads\n{threads_result}\nSeconds:{end_time-start_time}")


#Sum
start_time = time.time()
result = sum(array)
end_time = time.time()
    
print(f"Sum\n{result}\nSeconds:{end_time-start_time}")