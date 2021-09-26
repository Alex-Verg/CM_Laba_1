import math


class Polynom:
    coefficients = []
    d_coefficients = []

    def __init__(self, *coefs):
        self.coefficients = list(coefs)
        for i in range(1, len(self.coefficients)):
            self.d_coefficients.append(self.coefficients[i] * i)

    def function(self, x):
        f = 0
        variable = 1
        for a in self.coefficients:
            f += a * variable
            variable *= x

        return f

    def derivative(self, x):
        df = 0
        variable = 1
        for a in self.d_coefficients:
            df += a * variable
            variable *= x

        return df

    def sec_derivative(self, x):
        ddf = 0
        variable = 1
        for i in range(1, len(self.d_coefficients)):
            ddf += self.d_coefficients[i] * variable
            variable *= x

        return ddf

    def bisection_method(self, a, b, epsilon):
        x = (a + b) / 2
        while math.fabs(b-a) > epsilon or math.fabs(self.function(x)) > epsilon:
            if self.function(a) * self.function(x) <= 0:
                b = x
            else:
                a = x
            x = (a + b)/2

        return x

    def chord_method(self, a, b, epsilon):
        f_a = self.function(a)
        f_b = self.function(b)
        x_prev = 1000000  # float('-inf')
        x = (a * f_b - b * f_a) / (f_b - f_a)
        f_x = self.function(x)
        while math.fabs(f_x) > epsilon or math.fabs(x-x_prev) > epsilon:
            if f_a * f_x < 0:
                f_b = f_x
                b = x
            else:
                f_a = f_x
                a = x
            x_prev = x
            x = (a * f_b - b * f_a) / (f_b - f_a)
            f_x = self.function(x)

        return x

    def newtons_method(self, a, b, epsilon):
        if self.function(a) * self.sec_derivative(a) > 0:
            x = a
        else:
            x = b

        dx = self.function(x) / self.derivative(x)

        while math.fabs(dx) > epsilon or math.fabs(self.function(x)) > epsilon:
            x -= dx
            dx = self.function(x) / self.derivative(x)
            print(x, self.function(x))

        return x


if __name__ == "__main__":
    var = Polynom(6, -4, 2, 1, -3, 2)
    print(var.chord_method(-2, 0, 1e-5))
    print(var.function(-1.2197348640894328))


elif __name__ == "__init__":
    pass
