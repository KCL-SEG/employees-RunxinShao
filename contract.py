from abc import ABC, abstractmethod


class Contract:
    @abstractmethod
    def get_pay(self):
        pass


class MonthlyContract(Contract):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'monthly salary of {self.get_pay()}'

    def get_pay(self):
        return self.amount


class HourlyContract(Contract):
    def __init__(self, hours, hour_pay):
        self.hours = hours
        self.hour_pay = hour_pay

    def get_pay(self):
        return self.hours * self.hour_pay

    def __str__(self):
        return f'contract of {self.hours} hours at {self.hour_pay}/hour'
