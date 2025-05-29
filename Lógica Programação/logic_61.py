# Decoradores com parâmetros.

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhado(*args, **kwargs):
            print('Parametro decorador: ', a, b, c)
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhado
    return fabrica_de_funcoes

@fabrica_de_decoradores
def soma(x, y):
    return x + y

multiplicar = fabrica_de_decoradores()(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplicar(10, 5)

print(dez_mais_cinco)
print(dez_vezes_cinco)