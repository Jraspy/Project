# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = 1

    def __add__(self, other):
        return self.a + self.b * self.i + other.a + other.b * other.i

    def __mul__(self, other):
        return (self.a + self.b * self.i) * (other.a + other.b * other.i)


complex_Num1 = ComplexNumber(2, 3)
complex_Num2 = ComplexNumber(1, 1)
print(f"Результат сложения: {(complex_Num1 + complex_Num2)}")
print(f"Результат умножения: {(complex_Num1 * complex_Num2)}")


# Вариант 2. Использование встроенного типа данных complex:
a = input("Введите число1 :")
b = input("Введите число2 :")
a = complex(a)
b = complex(b)
print(f"Результат сложения: {a + b}")
print(f"Результат умножения: {a * b}")

# Output:
# Результат сложения: 7
# Результат умножения: 10
# Введите число1 :2
# Введите число2 :3
# Результат сложения: (5+0j)
# Результат умножения: (6+0j)
#
# Process finished with exit code 0