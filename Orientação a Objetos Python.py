# ATIVIDADE 1 

# print ('-='*20)
# print ('---INICIO---')
# class Carro:
#     def __init__(self, marca, modelo, ano, funcionamento = False, cambio = False, velocidade = 120):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.velocidade = velocidade
#         self.funcionamento = funcionamento
#         self.cambio = cambio
 
#     def ligar (self):
#         if (self.funcionamento == False):
#             self.funcionamento = True
#         return'Já está ligado!'
        
#     def acelerar (self, valor):
#         if (self.funcionamento == False):
#             return 'Você precisa ligar o carro!'
#         elif (self.velocidade + valor) <= 120:
#             self.velocidade += valor
#             return self.velocidade
#         else:
#             return 'Você não pode passar de 120!!'
           
#     def desligar (self, funcionamento):
#         self.funcionamento = False
        
#     def veriMarcha (self):
#         if (0 <= self.velocidade and self.velocidade <= 20):
#             return 'marcha 1'
#         elif (20 < self.velocidade and self.velocidade <= 30):
#             return 'marcha 2'
#         elif (30 < self.velocidade and self.velocidade<= 35):
#             return 'marcha 3'
#         elif (35 < self.velocidade and self.velocidade <= 50):        
#             return 'marcha 4' 
#         elif (60 <= self.velocidade):    
#             return 'marcha 5'
        


# carroClassic = Carro('Chevrolet', 'Classic', '2012', False, False, 0)       

# # print (carroClassic.cambio)

# # Liga/ Desliga
# # 
# # 
# print (carroClassic.funcionamento)

# # Acelerar 

# print (carroClassic.velocidade)
# print (carroClassic.acelerar(130))

# # Desligar
# # carroClassic.desligar(False)
# # print(carroClassic.funcionamento)

# # VERIFICAR Marcha
# # print (carroClassic.veriMarcha())



### marca, modelo, ano, velocidade, liga/desliga, automatico/manual
### função liga, acelera, desliga, verifica marcha

 ## VERSÃO GI
# class Carro:
#     def __init__(self, marca, modelo, ano, velocidade, ligado = False, automatico = False, velocidadeMaxima = 130):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.velocidade = velocidade
#         self.ligado = ligado
#         self.automatico = automatico
#         self.velocidadeMaxima = velocidadeMaxima
        
#     def ligarDesligar(self):
#         if self.ligado == True:
#             self.ligado = False
#         self.ligado = True
        
#     # def acelerar (self, aceleracao):
#     #     if self.ligado == False:
#     #         return 'Ligue o carro'
#     #     elif (self.velocidade + aceleracao) < self.velocidadeMaxima:
#     #         self.velocidade += aceleracao
#     #     else:
#     #         return 'Velocidade máxima excedida!'
        
#     def verificaMarcha (self):
#         if self.velocidade <= 20:
#             return 'Marcha 1'
#         elif self.velocidade >= 21 and self.velocidade < 30:
#             return 'Marcha 2'
#         elif self.velocidade >= 30 and self.velocidade < 45:
#             return 'Marcha 3'
#         elif self.velocidade >= 45 and self.velocidade < 60:
#             return 'Marcha 4'
#         elif self.velocidade >= 60 and self.velocidade <= 120:
#             return 'Marcha 5'
#         else:
#             return 'Velocidade excedida'
        
        
# carro1 = Carro('Ford','Fusion',2019,130,False,True)
# print(carro1.ligado)
# carro1.ligarDesligar()
# print(carro1.ligado)

# print(carro1.velocidade)
# carro1.acelerar(100)
# print(carro1.velocidade)

# print(carro1.verificaMarcha())
# print(carro1.acelerar(50))
# carro1.acelerar(15)
# print(carro1.velocidade)


# ATIVIDADE 2



    
### atributos nome do pet, idade, gato ou cachorro
### TEMPO DE SUPERVISIONAMENTO, VALOR COBRADO