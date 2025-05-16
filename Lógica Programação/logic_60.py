# Funções decoradoras e decoradores
# Decorar = adicionar / remover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções.
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sungar" (Açúcar sintático).

def creat_function(func):
    def internal(*args, **kwargs):
        print('I will decorete you.')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'Your result was {result}')
        print('Ok, now you have been decorated')
        return result
    return internal

@creat_function
def reverse_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param is must be string')
    
reverse_string_checking_parameter = creat_function(reverse_string)
inverted = reverse_string_checking_parameter('123')