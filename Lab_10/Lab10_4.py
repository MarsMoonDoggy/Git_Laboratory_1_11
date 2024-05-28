from get_datetime import get_datetime
get_datetime()

class TypeCheckDecorator:
    def __init__(self, return_type):
        self.return_type = return_type

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, self.return_type):
                raise ValueError(f"Возвращаемое значение должно быть типа {self.return_type}, получен {type(result)}")
            return result

        return wrapper

@TypeCheckDecorator(str)
def get_greeting(name):
    return f"Привет, {name}!"

@TypeCheckDecorator(list)
def get_numbers(n):
    return list(range(n))


print(get_greeting("Вовочка"))
print(get_numbers(5))

try:
    print(get_greeting(123))
except ValueError as e:
    print(e)

try:
    print(get_numbers("abc"))
except ValueError as e:
    print(e)

