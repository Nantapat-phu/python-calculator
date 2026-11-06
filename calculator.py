class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        while b != 0:
            if b > 0:
                result = self.add(result, a)
                b = self.subtract(b, 1)
            else:
                result = self.subtract(result, a)
                b = self.add(b, 1)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Can not divided by zero"
        negative = (a < 0) != (b < 0)
        if a < 0:
            a = self.subtract(0, a)
        if b < 0:
            b = self.subtract(0, b)
        count = 0
        while a >= b:
            a = self.subtract(a, b)
            count = self.add(count, 1)
        return self.subtract(0, count) if negative else count
    
    def modulo(self, a, b):
        if b == 0:
            return "Can not divided by zero"
        divisor = self.subtract(0, b) if b < 0 else b
        r = self.subtract(0, a) if a < 0 else a
        while r >= divisor:
            r = self.subtract(r, divisor)
        if r != 0:
            if a < 0:
                r = self.subtract(divisor, r)
            if b < 0:
                r = self.add(r, b)
        return r

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: addition: ", calc.add(-1, -2))
    print("Example: subtraction: ", calc.subtract(6, 7))
    print("Example: subtraction: ", calc.subtract(-6, -7))
    print("Example: multiplication: ", calc.multiply(6, 7))
    print("Example: multiplication: ", calc.multiply(-6, -7))
    print("Example: division: ", calc.divide(6, 7))
    print("Example: division: ", calc.divide(6, 0))
    print("Example: modulo: ", calc.modulo(6, 7))
    print("Example: modulo: ", calc.modulo(-6, 7))