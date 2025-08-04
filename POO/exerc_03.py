# Exercício:
# Sistema bancario.


from abc import ABC, abstractmethod

# === CLASSES DE CONTA ===
class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0.0) -> None:
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Depósito de R${valor:.2f}')
        return self.saldo

    def detalhes(self, msg='') -> None:
        print(f'[Conta {self.numero}] Saldo: R${self.saldo:.2f} {msg}')

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(Agência: {self.agencia}, Conta: {self.numero}, Saldo: {self.saldo:.2f})'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        if self.saldo >= valor:
            self.saldo -= valor
            self.detalhes(f'Saque de R${valor:.2f}')
        else:
            print('❌ Saldo insuficiente para saque.')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero: int, saldo: float = 0.0, limite: float = 100.0) -> None:
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.detalhes(f'Saque de R${valor:.2f} (com limite)')
        else:
            print('❌ Limite excedido.')
        return self.saldo

    def __repr__(self) -> str:
        return f'{super().__repr__()}, Limite: R${self.limite:.2f}'


# === CLASSES DE PESSOA E CLIENTE ===
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(Nome: {self.nome}, Idade: {self.idade})'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None = None


# === CLASSE BANCO ===
class Banco:
    def __init__(self) -> None:
        self.clientes: list[Cliente] = []
        self.contas: list[Conta] = []
        self.agencias: list[int] = []

    def adicionar_cliente(self, cliente: Cliente, conta: Conta):
        cliente.conta = conta
        self.clientes.append(cliente)
        self.contas.append(conta)
        if conta.agencia not in self.agencias:
            self.agencias.append(conta.agencia)

    def autenticar(self, cliente: Cliente) -> bool:
        if cliente not in self.clientes:
            print('❌ Cliente não encontrado.')
            return False
        if cliente.conta not in self.contas:
            print('❌ Conta não encontrada.')
            return False
        if cliente.conta.agencia not in self.agencias:
            print('❌ Agência não autorizada.')
            return False
        return True


# === TESTE DO SISTEMA ===
if __name__ == '__main__':
    banco = Banco()

    c1 = Cliente('Lucas', 22)
    cc1 = ContaCorrente(agencia=101, numero=1001, saldo=50, limite=150)
    banco.adicionar_cliente(c1, cc1)

    c2 = Cliente('Ana', 30)
    cp1 = ContaPoupanca(agencia=101, numero=1002, saldo=200)
    banco.adicionar_cliente(c2, cp1)

    if banco.autenticar(c1):
        c1.conta.depositar(100)
        c1.conta.sacar(120)

    if banco.autenticar(c2):
        c2.conta.sacar(50)
        c2.conta.depositar(80)

    print(c1.conta)
    print(c2.conta)
