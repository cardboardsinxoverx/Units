# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Ln')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math
import numpy as np

import metpy.calc as mpcalc
from metpy.units import units


def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Fahrenheit to Celsius')
    print('4. Celsius to Fahrenheit')
    print('5. MPH to knots')
    print('6. Knots to MPH')


def km_miles():
    km = float(input('Enter a distance in kilometers:'))
    miles = km / 1.609
    print(miles)


def miles_km():
    miles = float(input('Enter a distance in miles:'))
    km = miles * 1.609
    print(km)


def fahrenheit_celsius():
    fahrenheit = float(input('Enter a temperature in Fahrenheit:'))
    fahrenheit = (celsius * 1.8) + 32 #defined FAHRENHEIT twice!!!
    print(celsius)


def celsius_fahrenheit():
    celsius = float(input('Enter a temperature in Fahrenheit'))
    celsius = (fahrenheit - 32) * 1.8
    print(fahrenheit)


choice = input('Which conversion would you like to perform?')

if choice == '1':
    km_miles()
if choice == '2':
    km_miles()
if choice == '3':
    fahrenheit_celsius()
if choice == '4':
    celsius_fahrenheit()