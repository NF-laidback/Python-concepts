# here we will see how just creating coroutines by using await keywords are not enough to 
# make the code concurrent (we have to create tasks from coroutines)

import asyncio
import time

async def fetch_data(number):
    print(f"do something with number {number}")

    await asyncio.sleep(number)

    print(f"Done with text {number}")

    return (f" Result is {number}")


async def main():
    task1 = fetch_data(2)
    task2 = fetch_data(3)

    result1 = await task1
    print("task1 succesfully completed")
    result2 = await task2
    print("task2 fully completed")

    return (result1, result2)


t1 = time.perf_counter()

result = asyncio.run(main())

print(result)

t2 = time.perf_counter()

print(f"total time taken for execution is {t2-t1}")