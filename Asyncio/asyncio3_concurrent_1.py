# here we will see how concurrent programming is done

# asyncio is Python's built-in library for writing concurrent code using
# coroutines (async/await) on a single thread.
import asyncio
# time is used here to measure how long the whole program takes to run.
import time

# "async def" defines a coroutine function. Calling it does not run the body
# right away; it returns a coroutine object that asyncio can schedule.
async def fetch_data(number):

    # Simulate starting some work. The number is printed so we can see which
    # task is running.
    print(f"do something with number {number}")
    # Pause this coroutine for `number` seconds. "await" hands control back to
    # the event loop, so other tasks can run while this one is sleeping.
    # (This stands in for a real I/O call such as a network request.)
    await asyncio.sleep(number)
    print(f"done with number {number}")

    # The value returned here becomes the result of the task / await.
    return (f"return ressult with number {number} ")

# main() is the top-level coroutine that creates and waits for the tasks.
async def main():
    # create_task() wraps each coroutine in a Task and schedules it on the
    # event loop immediately. All three run concurrently from this point on.
    # fetch_data(2) finishes after ~2 seconds, fetch_data(10) after ~10 seconds,
    # and fetch_data(3) after ~3 seconds.
    task1 = asyncio.create_task(fetch_data(2))
    task2 = asyncio.create_task(fetch_data(10))
    task3 = asyncio.create_task(fetch_data(3))

    # The "fully completed" messages below print in the order of the awaits,
    # not in the order the tasks finish. main() is one coroutine that waits on
    # task1, then task2, then task3, so the printing order depends on that
    # await order. For example, the "Task3 fully completed" line will only
    # print after the event loop has finished waiting on task2, because task2
    # is first in the await order and main() cannot move on until it is done,
    # even if task3 finished long before.

    # "await" waits for task1 to finish and stores its return value in result1.
    # Tasks 2 and 3 keep running in the background while we wait here.
    result1 = await task1
    print("Task 1 fully completed")

    # Wait for task2 (the slowest, ~10 seconds). Note that task3 may already
    # be finished by now, and it still has not been "lost": its result is
    # kept in the task until we await it below.
    result2 = await task2

    print("Task2 fully completed")

    # task3 is already done by this point, so this await returns immediately
    # with its stored result.
    result3 = await task3
    print("Task3 fully completed")

    # Return the three results together as a tuple.
    return(result1, result2, result3)

# Record the start time using a high-resolution clock.
t1 = time.perf_counter()

# asyncio.run() creates an event loop, runs main() to completion, and then
# closes the loop. Its return value is the tuple returned by main().
result = asyncio.run(main())

print(f"the results are {result}")

# Record the end time and print the elapsed time. Because the tasks run
# concurrently, the total is about 10 seconds (the longest task), not the
# 2 + 10 + 3 = 15 seconds it would take if they ran one after another.
t2 = time.perf_counter()

print(f"The time taken for execution is {t2-t1}")

