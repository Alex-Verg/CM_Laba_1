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
        print('-'*70 + '\n' + ' ' * 27 + 'Bisection method' + ' ' * 27 + '\n' + '-'*70)
        x = (a + b) / 2
        iters = 0
        while math.fabs(b-a) > epsilon or math.fabs(self.function(x)) > epsilon:
            if self.function(a) * self.function(x) <= 0:
                b = x
            else:
                a = x
            x = (a + b)/2
            iters += 1
            print(iters, 'iteration, a =', round(a, 6), 'b =', round(b, 6), 'f(a) =', round(self.function(a), 6), 'f(b) =', round(self.function(b), 6))
        print('Number of iterations:', iters)

        return x

    def chord_method(self, a, b, epsilon):
        print('-'*70 + '\n' + ' ' * 28 + 'Hordes method' + ' ' * 29 + '\n' + '-'*70)
        f_a = self.function(a)
        f_b = self.function(b)
        x_prev = 1000000
        x = (a * f_b - b * f_a) / (f_b - f_a)
        f_x = self.function(x)
        iters = 0
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
            iters += 1
            print(iters, 'iteration, a =', round(a, 6), 'b =', round(b, 6), 'f(a) =', round(f_a, 6), 'f(b) = ', round(f_b, 6))
        print('Number of iterations:', iters)

        return x

    def newtons_method(self, a, b, epsilon):
        print('-'*70 + '\n' + ' ' * 26 + 'Newton\'s method' + ' ' * 27 + '\n' + '-'*70)

        if self.function(a) * self.sec_derivative(a) > 0:
            x = a
        else:
            x = b

        dx = self.function(x) / self.derivative(x)
        iters = 0

        while math.fabs(dx) > epsilon or math.fabs(self.function(x)) > epsilon:
            x -= dx
            dx = self.function(x) / self.derivative(x)
            iters += 1
            print(iters, 'iteration, x =', x, 'f(x) =', self.function(x))
        print('Number of iterations:', iters)

        return x


if __name__ == "__main__":
    var = Polynom(6, -4, 2, 1, -3, 2)
    print('x =', round(var.bisection_method(-2, -1, 1e-5), 5))
    print('x =', round(var.chord_method(-2, -1, 1e-5), 5))
    print('x =', round(var.newtons_method(-2, -1, 1e-5), 5))

elif __name__ == "__init__":
    pass
