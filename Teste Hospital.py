from Hospital import Medico
from Hospital import Auxiliar
from Hospital import Cirurgiao

print('-='*20)
print('-----INICIO-----')

medico = Medico('12345', 'Otavio', 55, 60000)
auxiliar = Auxiliar('54321', 'Ana', 60, 40000)
cirurgiao = Cirurgiao('67890', 'Alex', 50, 50000)

medico1 = Medico('23456', 'Sergio', 40, 20000)
auxiliar1 = Auxiliar('65432', 'Vitor', 30, 30000)
cirurgiao1 = Cirurgiao('78901', 'Elena', 35, 25000)

print ('Medico 1 ', medico.__nome, medico.aposentadoria())
print ('Medico 2 ', medico1.__nome, medico1.aposentadoria())
print ('Auxiliar 1 ', auxiliar.__nome, auxiliar.aposentadoria())
print ('Auxiliar 2 ', auxiliar1.__nome, auxiliar1.aposentadoria())
print ('Cirurgião 1 ', cirurgiao.__nome, cirurgiao.aposentadoria())
print ('Cirurgião 2 ', cirurgiao1.__nome, cirurgiao1.aposentadoria())

