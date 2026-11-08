def type_check(*args_types):
    def decorator(func):
        def wrapper(*args):
            i = 0
            if len(args) != len(args_types):
                assert False,  f"Ожидалось аргументов: {len(args_types)}, получено: {len(args)}"
            for arg, expected_type in zip(args, args_types):
                assert isinstance(arg, expected_type), "TypeError"
            return func(*args)
        return wrapper
    return decorator


@type_check(int,int)
def check_type(a,b):
    return a+b

print(check_type(1,1))