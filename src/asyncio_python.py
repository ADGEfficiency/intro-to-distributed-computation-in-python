import asyncio
import time


async def long_running_task():
    print("one")
    #  have to use special, non-blocking, async method here
    await asyncio.sleep(1)
    print("two")

    
async def main():
    await asyncio.gather(long_running_task(), long_running_task(), long_running_task())
    
    
if __name__ == "__main__":
    s = time.perf_counter()
    # requires Python 3.7 & above
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print('executed in {:0.2f} seconds'.format(elapsed))
