from abc import ABCMeta, abstractmethod
from select import select
import string


class CashSuper(metaclass=ABCMeta):

    @abstractmethod
    def acceptCash(price: float) -> float:
        pass


class CashNormal(CashSuper):

    def acceptCash(self, price: float) -> float:
        return price


class CashRebate(CashSuper):

    MoneyRebate = 1.00

    def cashRebate(self, Rebate):
        self.MoneyRebate = Rebate

    def acceptCash(self, price: float) -> float:
        return price * self.MoneyRebate


class CashMoneyOff(CashSuper):
    moneyCondition = 0.00
    moneyReturn = 0.00

    def cashMoneyOff(self, moneyCondition, moneyReturn):
        self.moneyCondition = moneyCondition
        self.moneyReturn = moneyReturn

    def acceptCash(self, price: float) -> float:
        if price >= self.moneyCondition:
            return price - (price // self.moneyCondition) * self.moneyReturn
        else:
            return price


class CashContext:
    cs = None

    def cash_context(self, mode: string = ''):
        if mode == "打折":
            cs = CashRebate()
            cs.cashRebate(0.8)
            
        elif mode == "满减":
            cs = CashMoneyOff()
            cs.cashMoneyOff(200, 100)
        else:
            cs = CashNormal()
            
        self.cs = cs

    def result(self, money):
        return self.cs.acceptCash(1000)


if __name__ == '__main__':
    # cs = CashFactory.create_cash_factory("打折")
    # cs.cashRebate(0.8)

    # cs = CashFactory.create_cash_factory("满减")
    # cs.cashMoneyOff(200, 100)

    cs = CashContext()
    cs.cash_context(mode="满减")
    res = cs.result(1000)
    print(res)
