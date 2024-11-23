def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов аргументов декорируемой функции
        annotations = func.__annotations__

        # Проверяем количество переданных аргументов и количество возвращаемых
        if len(args) + len(kwargs) + int('return' in annotations) != len(annotations):
            raise TypeError(f"Expected {len(annotations) - int('return' in annotations)} arguments, got {len(args) + len(kwargs)}")

        # Проверяем типы
        for arg_name, arg_value in zip(annotations.keys(), args):
            if not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f"Argument '{arg_name} must be of type {annotations[arg_name].__name__}.")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# Примеры использования
#print(sum_two(1, 2))  # >>> 3
#print(sum_two(1, 2, 3))  # >>> TypeError
#print(sum_two(1, 2.4))  # >>> TypeError
