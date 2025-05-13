# Entendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo.
# O Python conhece a pasta onde o __main__ está e as portas abaixo dele.
# Ele não reconhece portas e módulos acima do __main__ por padrão.
# O Python conhece todos os módulos e pacotes presentes nos caimnhas sys.path

import logic_57_m

print('Este módulo se chama', __name__)
