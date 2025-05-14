# Entendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo.
# O Python conhece a pasta onde o __main__ está e as portas abaixo dele.
# Ele não reconhece portas e módulos acima do __main__ por padrão.
# O Python conhece todos os módulos e pacotes presentes nos caimnhas sys.path

import logic_57_m
from logic_57_m import soma

# print('Este módulo se chama', __name__)

print(logic_57_m.variavel_modulo)

print(logic_57_m.soma(2, 2))
print(soma(3, 3))