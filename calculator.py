class Calculator:
    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Нельзя делить на ноль")
        return a / b
