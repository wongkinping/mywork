import math
import matplotlib.pyplot as plt


M = 0.1
k = 10
g = 9.8
lamb = 0.7
T = 0.1
dt = 0.001
x2 = 2


x_array = []
y_array = []


def f(x, v):
    return -k / M*x + g - lamb / M*v

def xfinal(v, callback=None, inclusive=False):
    x = 0

    end = math.floor(T / dt)
    if inclusive:
        end += 1

    for i in range(0, end):
        if callback:
            callback(i, dt, x)

        f0 = f(x, v)
        v0 = v

        f1 = f(x + 0.5*dt*v0, v + 0.5*dt*f0)
        v1 = v + 0.5*dt*f0

        f2 = f(x + 0.5*dt*v1, v + 0.5*dt*f1)
        v2 = v + 0.5*dt*f1

        f3 = f(x + dt*v2, v + dt*f2)
        v3 = v + dt*f2

        dx = 1/6 * dt * (v0 + 2*(v1+v2) + v3)
        dv = 1/6 * dt * (f0 + 2*(f1+f2) + f3)

        x += dx
        v += dv
    return x


def F(v):
    return xfinal(v) - x2

def my_callback(i, dt, x):
    x_value = i * dt
    y_value = x
    print('{} {}'.format(x_value, y_value))
    x_array.append(x_value)
    y_array.append(y_value)


def main():
    a = 0
    b = 100
    
    for i in range(0, 100):
        c = (a + b) / 2
        if F(a) * F(c) < 0:
            b = c
        else:
            a = c

    v = a
    xfinal(v, my_callback, inclusive=True)
    plt.plot(x_array, y_array)
    plt.savefig('output.png', format='png')


if __name__ == '__main__':
    main()
