import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f"{name} started at: {timer():.2f}s")
    await asyncio.sleep(seconds)
    print(f"{name} completed at: {timer():.2f}s")

async def main():
    start = timer()
    await asyncio.gather(
        run_task("Task 1", 2),
        run_task("Task 2", 1),
        run_task("Task 3", 3)
    )
    print(f"\nTotal time taken: {timer() - start:.2f}s")

asyncio.run(main())