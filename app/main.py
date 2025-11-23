from typing import Callable

def cache(func: Callable) -> Callable:
    memory_dict = {}
    
    def wrapper(*args, **kwargs) -> int:
        if args in memory_dict:
            return memory_dict[args]
        else:
            result = func(args)
            memory_dict[args] = result
            return result
    return wrapper
