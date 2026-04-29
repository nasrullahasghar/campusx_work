import time
from timeit import default_timer as timer

def run_task(name, seconds):
    print(f"{name} started at: {timer():.2f}s")
    time.sleep(seconds)
    print(f"{name} completed at: {timer():.2f}s")

start = timer()

run_task("Task 1", 2)
run_task("Task 2", 1)
run_task("Task 3", 3)

print(f"\nTotal time taken: {timer() - start:.2f}s")