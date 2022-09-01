from numpy import atleast_1d, poly1d
from pint import matplotlib
from sympy.abc import z, y, x, f, m, a


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math
from sympy import diff, sin, exp, integrate
from sympy.abc import x, y
from scipy.interpolate import InterpolatedUnivariateSpline
import numpy.core.numeric as NX
import sympy as sym
import numpy as np
import metpy.calc as mpcalc
from metpy.units import units
import matplotlib.pyplot as plt
import matplotlib as mpl
import units as u
import basic_units
from random import randint


# basic units
#
## ampere
# print(u.Unit(randint(1, 100), u.ampere))
## candela
# print(u.Unit(randint(1, 100), u.candela))
## kelvin
# print(u.Unit(randint(1, 100), u.kelvin))
## kilogram
# print(u.Unit(randint(1, 100), u.kilogram))
## meter
# print(u.Unit(randint(1, 100), u.metre))
## mole
# print(u.Unit(randint(1, 100), u.mole))
## second
# print(u.Unit(randint(1, 100), u.second))
#
## arbitrary derived units

speed = u.DerivedUnit.define('speed', u.metre / u.second)
v = u.Unit(10, speed)

## this equation is needed for the input range error in the choice section below
a = np.arange(1, 11, 1)


# conversion menu
def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometer')
    print('3. Fahrenheit to Celsius')
    print('4. Celsius to Fahrenheit')
    print('5. MPH to Knots')
    print('6. Knots to MPH')
    print('7. Pounds to Kilograms')
    print('8. Kilograms to Pounds')
    print('9. Sine Curve Plot')
    print('10. Radians to Degrees')
    print('11. Exit Program')


# 1
def km_miles():
    km = float(input('Enter a distance in kilometers: '))
    miles = km / 1.609
    print("{:.2f} miles".format(miles))


# 2
def miles_km():
    miles = float(input('Enter a distance in miles: '))
    km = miles * 1.609
    print("{:.2f} kilometers".format(km))


# 3
def fahrenheit_celsius():
    fahrenheit = float(input('Enter a temperature in Fahrenheit: '))
    celsius = (fahrenheit - 32) * (5 / 9)
    print("{:.2f}°C".format(celsius))


# 4
def celsius_fahrenheit():
    celsius = float(input('Enter a temperature in Celsius: '))
    fahrenheit = (celsius * (9 / 5)) + 32
    print("{:.2f}°F".format(fahrenheit))


# 5
def mph_knots():
    mph = float(input('Enter a wind speed in miles per hour: '))
    knots = mph * 0.868976
    print("{:.2f} knots".format(knots))


# 6
def knots_mph():
    knots = float(input('Enter a wind speed in knots: '))
    mph = knots * 1.150779
    print("{:.2f} miles per hour".format(mph))


# 7
def lbs_kg():
    lbs = float(input('Enter a weight in pounds: '))
    u.kilogram = (lbs / 2.205)
    print("{:.2f} kilograms".format(u.kilogram))


# 8
def kg_lbs():
    u.kilogram = float(input('Enter a weight in kilograms: '))
    lbs = u.kilogram * 2.20462
    print("{:.2f} pounds".format(lbs))


# 9
def sine_curve_plot():
    # coordinates section, these variable equations can be recycled
    n = float(input('Enter in x_min for graph '))
    m = float(input('Enter in x_max for graph '))
    p = float(input('Enter in x_interval for graph '))
    sin_var_x = np.arange(n * np.pi, m * np.pi, p)
    sin_var_y = np.sin(sin_var_x)

    # plotting section
    plt.plot(sin_var_x, sin_var_y)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Sine Wave')
    plt.legend(['Sine'])
    plt.show()
# 10

basic_units.rad_fn(x)
x = float(input('Enter in x'))


## 11 indefinite integral of a polynomial
# def polyint(p, m=1, k=None):
#    m = int(m)
#
#
# if m < 0:
#    raise ValueError("Order of integral must be positive")
# if k is None:
#    k = np.zeros(m, float)
# k = atleast_1d(k)
# if len(k) == 1 and m > 1:
#    k = k[0] * np.ones(m, float)
# if len(k) < m:
#    raise ValueError("k must be a scalar or rank-1 array of length 1 or greater than m")

# choice sectioning
if __name__ == '__main__':
    print_hi('Ln')
    exit = False
    while not exit:
        print_menu()

        choice = int(input('Which conversion would you like to perform? '))

        if choice == 1:
            km_miles()
        elif choice == 2:
            km_miles()
        elif choice == 3:
            fahrenheit_celsius()
        elif choice == 4:
            celsius_fahrenheit()
        elif choice == 5:
            mph_knots()
        elif choice == 6:
            knots_mph()
        elif choice == 7:
            lbs_kg()
        elif choice == 8:
            kg_lbs()
        elif choice == 9:
            sine_curve_plot()
        elif choice == 10:
            basic_units.rad_fn()
        elif choice == 11:
            print('Once tested, thus infected!')
            exit = True
        elif choice != a.any():
            print('Please enter in a number from 1 to 10')
