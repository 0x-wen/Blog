"""
# 各类打折活动的工厂模式设计、打折、满减等
1.抽象收费对象基类 
    - 现金收费 interface args(原价) -> return 优惠价
2.打折类 args(折扣)
3.满减类

# 思考: 付款后 要根据付款金额累计积分 如何设计呢？
    - CashSuper 基类 新增计算积分的 interface,  其子类都要实现算积分的方法,不是最优解
"""


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


class CashFactory:

    def create_cash_factory(mode: string = ''):
        if mode == "打折":
            cs = CashRebate()
        elif mode == "满减":
            cs = CashMoneyOff()
        else:
            cs = CashNormal()
        return cs


if __name__ == '__main__':
    # cs = CashFactory.create_cash_factory("打折")
    # cs.cashRebate(0.8)
    
    # cs = CashFactory.create_cash_factory("满减")
    # cs.cashMoneyOff(200, 100)

    cs = CashFactory.create_cash_factory()
    res = cs.acceptCash(1000)
    print(res)
