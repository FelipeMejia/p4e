import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        elapsed = time.time() - self.start
        print(f"Elapsed time: {elapsed: .3f} seconds")


with Timer() as timer:
    time.sleep(3)
