"""Простое приложение-калькулятор для демонстрации CI/CD"""


class Calculator:
    def add(self, a: float, b: float) -> float:
        """Сложение"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Вычитание"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Умножение"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Деление"""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Возведение в степень"""
        return a ** b

    def sqrt(self, a: float) -> float:
        """Квадратный корень"""
        if a < 0:
            raise ValueError("Cannot take sqrt of negative number")
        return a ** 0.5


if __name__ == "__main__":
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"3 * 4 = {calc.multiply(3, 4)}")
    print(f"12 / 4 = {calc.divide(12, 4)}")
    print(f"2 ^ 3 = {calc.power(2, 3)}")
    print(f"sqrt(16) = {calc.sqrt(16)}")
