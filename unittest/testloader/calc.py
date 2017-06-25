class Calc:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 定义加法
    def add(self):
        return self.a + self.b

    # 定义减法
    def sub(self):
        return self.a - self.b

    # 定义乘法
    def mul(self):
        return self.a * self.b

    # 定义除法
    def div(self):
        return self.a / self.b


