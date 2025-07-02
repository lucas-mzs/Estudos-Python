# from log import LogPrintMixin, LogFileMixin

# lp = LogPrintMixin()
# lp.log_error('qualquer coisa')
# lp.log_success('Que legal')

# lf = LogFileMixin()
# lf.log_error('qualquer coisa')
# lf.log_success('Que legal')

from elotronico import SmartPhone

galaxy_s = SmartPhone('Galaxy S')
iphone = SmartPhone('iPhone')

galaxy_s.ligar()
iphone.desligar()