from functools import wraps
import time

def WongWongTimer(func):
    @wraps(func)
    def wrap(*args, **kargs):
        time_start = time.time()
        value = func(*args, **kargs)
        time_end = time.time()
        time_spend = time_end - time_start
        #print(f"[{func.__module__}.{func.__name__}] cost time: {time_spend}")
        print(f"[{func.__qualname__}] cost time: {time_spend}")

        return value

    return wrap


def WongWongDebugger(func):
    @wraps(func)
    def wrap(*args, **kargs):
        print(f"[wongwong_logger][start func][{func.__qualname__}()] args: {args}, kargs: {kargs}")
        value = func(*args, **kargs)
        print(f"[wongwong_logger][end func][{func.__qualname__}()] successfully finished!!!")

        return value

    return wrap
