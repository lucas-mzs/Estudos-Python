# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# modo Pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ele é um método que se comporta como um atributo.
# Geralmente é usada nas seguintes situações:
# - como getter;
# - para evitar quebrar código cliente;
# - para habilitar setter;
# - para executar ações ao obter um atributo.
# código cliente -  é o código que usa o seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPETRY')
        return self.cor_tinta
    
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)


################################################


# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor
    
# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())