# Funções decoradoras e decoradores
# Decorar = adicionar / remover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções.
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sungar" (Açúcar sintático).

def criadora_de_funcao(func):
    def interna(*args, **kwargs):
        print('Eu vou decorar você.')
        for arg in args:
            é_string(arg)
        resultado = func(*args, **kwargs)
        print(f'Seu resultado foi {resultado}')
        print('Ok, agora você foi decorado.')
        return resultado
    return interna

@criadora_de_funcao
def reverter_string(string):
    return string[::-1]

def é_string(param):
    if not isinstance(param, str):
        raise TypeError('parâmetro deve ser string')
    
parametro_de_verificacao_de_string = criadora_de_funcao(reverter_string)
inverter = parametro_de_verificacao_de_string('123')