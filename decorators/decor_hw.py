from datetime import datetime
import os



def logging(arg):
    path = arg

    def outer(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not any(args):
                arguments = kwargs
            elif not any(kwargs):
                arguments = args
            else:
                arguments = args, kwargs
            with open(f'{path}logger.txt', 'a+', encoding='utf-8') as f:
                start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer = f.write(f'Name: {func.__name__}, arguments: {arguments},'
                                 f' call_time: {start}, result: {result}\n')
                return result
        return wrapper
    return outer


@logging('C:/Users/Ярослав/PycharmProjects/pythonProject/decorators/')
def some_func(*args, **kwargs):
    print('Выполнено суммирование аргументов')
    return sum(args)


@logging('C:/Users/Ярослав/PycharmProjects/pythonProject/decorators/')
def name_printing(*args, **kwargs):
    return args, kwargs


if __name__ == '__main__':
    some_func(1, 1, 1)
    some_func(1, 2, 3, 4, 5)
    name_printing(1, first_name='Max', lastname='Hodokov')
