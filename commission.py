from abc import ABC, abstractmethod



class Commission:
    @abstractmethod
    def get_pay(self):
        pass


class BonusCommission(Commission):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f' and receives a bonus commission of {self.get_pay()}.'

    def get_pay(self):
        return self.amount


class ContractCommission(Commission):

    def __init__(self, number_of_contract, contract_pay):
        self.number_of_contracts = number_of_contract
        self.contract_pay = contract_pay

    def get_pay(self):
        return (self.number_of_contracts * self.contract_pay)

    def __str__(self):
        return f' and receives a commission for {self.number_of_contracts} contract(s) at {self.contract_pay}/contract.'
