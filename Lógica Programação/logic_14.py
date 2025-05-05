# CONSTANTE = "Variáveis" que não vão mudar 
# Muitas condições no mesmo if (ruim)
#     <- Contagem de complexidade (ruim)

velocidade = 51 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGER = 1 # a distância onde o radar pega

vel_carro_pas_rad_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and local_carro <= (LOCAL_1 + RADAR_RANGER)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pas_rad_1

if vel_carro_pas_rad_1:
    print('Acima de velocidade')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')