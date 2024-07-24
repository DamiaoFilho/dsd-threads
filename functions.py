import concurrent.futures



def createThread(start, end, iterable):
    array = iterable[start:end]
    return  sum(array)


def calculate_with_threads(array, threads):
    lenght = len(array)

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
            

    return sum(threads_sum)