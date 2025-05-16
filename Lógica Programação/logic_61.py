# Decoradores com parâmetros.

def decorators_factory(a=None, b=None, c=None):
    def functions_factory(func):
        print('Decoradora 1')

        def nested(*args, **kwargs):
            print('Decorator parameter: ', a, b, c)
            print('Nested')
            res = func(*args, **kwargs)
            return res
        return nested
    return functions_factory

@decorators_factory
def sum(x, y):
    return x + y

multiply = decorators_factory()(lambda x, y: x * y)

ten_more_five = sum(10, 5)
ten_times_five = multiply(10, 5)

print(ten_more_five)
print(ten_times_five)