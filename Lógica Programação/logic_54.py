# try, finally e else

try:
    print('ABRIR ARQUIVO')
    # 8 / 0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')