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
        ...
    
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Depósito de R${valor:.2f}')
        return self.saldo
    
    def detalhes(self, msg='') -> None:
        print(f'[Conta {self.numero}] Saldo: R${self.saldo:.2f} {msg}')
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(Agência: {self.agencia}, Conta: {self.numero}, Saldo: {self.saldo:.2f})'
    
class ContaPoupanca(Conta):
    def sacar(self, valor:float) -> float:
        if self.saldo >= valor:
            self.saldo -= valor
            self.detalhes(f'Saque de R${valor:.2f}.')
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
            self.detalhes(f'Saque de R${valor:.2f} (com limte).')
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