def cache(func):
    memory = {}
    def wrapper(*args):
        if args not in memory:
            memory[args] = func(*args)
        return memory[args]
    return wrapper    

@cache
def sum(a:int,b:int):
    print("Сохранено в кэш")
    return a+b


print(sum(1,2))
print(sum(1,2))