# Ordem dos decoradores

def decorator_parameters(name):
    def decorator(func):
        print('Decoretor: ', name)

        def your_new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            end = f'{res} {name}'
            return end
        return your_new_function
    return decorator

@decorator_parameters(name='5')
@decorator_parameters(name='4')
@decorator_parameters(name='3')
@decorator_parameters(name='2')
@decorator_parameters(name='1')
def sum(x, y):
    return x + y

ten_more_five = sum(10, 5)
print(ten_more_five)