# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(f'{nome}, você ligando para {self.phone}')
        return 2134
    
call = CallMe('24999300707')
retorno = call('Luiz Ótavio')
print(retorno)