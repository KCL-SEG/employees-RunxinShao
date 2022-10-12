"""Employee pay calculator."""
from contract import *
from commission import *


class Employee:
    def __init__(self, name, Contract, Commission):
        self.name = name
        self.Commission = Commission
        self.Contract = Contract

    def get_pay(self):
        total_pay = 0
        total_pay += self.Contract.get_pay()
        if self.Commission :
            total_pay += self.Commission.get_pay()
        return total_pay
        #return self.Contract.get_pay() if self.Commission else (self.Contract.get_pay() + self.Commission.get_pay())


    def __str__(self):
        return f'{self.name} works on a {self.Contract}{self.Commission if self.Commission else "."} Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000), None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(100, 25), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(120, 30), BonusCommission(600))
print(billie)
print(charlie)
print(renee)
print(jan)
print(robbie)