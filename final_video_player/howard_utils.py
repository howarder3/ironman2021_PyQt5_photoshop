from functools import wraps

def howard_timer(func):
    @wraps(func)
    def wrap(*args, **kargs):
        time_start = time.time()
        func(*args, **kargs)
        time_end = time.time()
        time_spend = t_end - t_start
        print(f"[{func.__name__}] cost time: {time_spend}")

    return wrap
