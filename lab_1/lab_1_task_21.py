import time as tm

def timer(func):
    def wrapper(*args):
        start = tm.perf_counter()
        result = func(*args)
        end = tm.perf_counter()
        print(f"Время затраченное на программ: {end - start}")
        return result
    return wrapper

@timer
def sum(a,b):
    return a+b


print(sum(1,2))