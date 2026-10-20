## this code is for showing the time taken in synchonous programming

import time

def sample_function(text):

    print(f"starting sample_function with text {text}")

    time.sleep(10)

    print(f"the sample_function has returned text {text}\n\n")
    return(f" result is {text}")


def main():
    result1 = sample_function("running sample_function for 1st time")
    print(f"sample_function run for the first time")

    result2 = sample_function("running sample_function for 2nd time") 
    print(f"sample_function run for the second time time")

    return((result1, result2))


t1 = time.perf_counter()

results = main()

print(results)

t2 = time.perf_counter()

print(f"time taken to completely execute the code is {t2-t1} seconds")

