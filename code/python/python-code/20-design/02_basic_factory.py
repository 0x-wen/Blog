# 实现一个可维护 高扩展的 两数操作计算器
# 新增 * / 不会影响原代码逻辑

from abc import abstractmethod


class Operation:
    _numberA = 0
    _numberB = 0

    @abstractmethod
    def result(self, *args, **kwargs):
        pass

    def set_numberA(self, num):
        self._numberA = num

    def set_numberB(self, num):
        self._numberB = num


class OperationAdd(Operation):

    def result(self, *args, **kwargs):
        return self._numberA + self._numberB


class OperationSub(Operation):
    def result(self, *args, **kwargs):
        return self._numberA + self._numberB


class OperationFactory:

    def __init__(self, operation: str):
        if operation == "+":
            self.oper = OperationAdd()
        elif operation == "-":
            self.oper = OperationSub()

    def __call__(self, numA, numB):
        self.oper.set_numberA(numA)
        self.oper.set_numberB(numB)
        return self.oper.result()


if __name__ == '__main__':
    oper = OperationFactory("+")
    res = oper(1, 5)
    print(res)
