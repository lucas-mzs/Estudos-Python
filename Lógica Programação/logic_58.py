import importlib

import logic_58_m

print(logic_58_m.variavel)

for i in range(10):
    importlib.reload(logic_58_m)
    print(i)

print('FIM')