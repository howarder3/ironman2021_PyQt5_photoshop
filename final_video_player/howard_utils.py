from functools import wraps
import time

def howard_timer(func):
    @wraps(func)
    def wrap(*args, **kargs):
        time_start = time.time()
        value = func(*args, **kargs)
        time_end = time.time()
        time_spend = time_end - time_start
        print(f"[{func.__name__}] cost time: {time_spend}")

        return value

    return wrap
