import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    # time.sleep is a synchronous call. It blocks the whole thread, and the
    # event loop runs on that same thread, so it cannot switch to another task
    # while this one is sleeping. Think of it like an HTTP request made with a
    # blocking client such as requests.get(url): the program just waits on the
    # socket, and no other coroutine gets a chance to run.
    #
    # Being inside `async def` does not change this. A coroutine only gives
    # control back to the loop at an `await`. Here, task1 runs to completion
    # before task2 even starts, so the two "requests" run one after the other
    # (about 3 seconds in total, not 2).
    #
    # The non-blocking version is `await asyncio.sleep(param)`, or an async HTTP
    # client such as aiohttp. Those `await` points let the loop run the other
    # task while this one waits on the network.
    time.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")
