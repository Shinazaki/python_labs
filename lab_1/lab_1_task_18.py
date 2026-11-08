from datetime import datetime
def log_calls(filename: str):
    def decorator(func):
        def wrapper(*args):
            time = datetime.now()
            with open(filename, mode="a", encoding="utf-8") as f:
                f.write(f"Время вызова{time}, {args}\n")
            return func(*args)
        return wrapper
    return decorator

@log_calls("info.txt")
def sum(a,b):
    return a+b

sum(1,2)