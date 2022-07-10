from conta import Conta
from cliente import Cliente

conta = Conta(123, "Nico", 55.0, 1000.0)

conta2 = Conta(321,"Marco",100.0,1000.0)


conta.extrato()
conta2.extrato()
print(".......................................")
conta2.transfere(10.0, conta)

conta2.extrato()
conta.extrato()

client = Cliente('matheus')

print(client.nome)

client.nome = 'nico'

conta.saca(1200)

conta.saca(100)

#Chamando o Garbage Colector
client = None