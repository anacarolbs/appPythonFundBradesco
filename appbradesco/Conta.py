class Conta:
    def __init__(self, titular, numero):
        self.saldo=0
        self.numero = numero
        self.titular = titular

# A função Property deve ser utilizada somente se você precisar da funcionalidade de transformar ou
        # verificar um atributo quando ele é atribuído ou lido.

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            if (saldo<0):
                print("O saldo não pode ser negativo")
            else:
                self._saldo = saldo

        def saque(self, valor):
            if(self.saldo>=valor):
                self.saldo-=valor
                print("Saque realizado com sucesso")
            else:
                print("Saldo insuficiente")

        def deposita(self, valor):
            self.saldo+=valor

        def extrato(self):
            print("Cliente: ", self.titular, "Saldo Atual: ", self._saldo)

