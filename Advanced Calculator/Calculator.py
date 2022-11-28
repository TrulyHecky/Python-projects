import math
from math import pi

class Calculator():
    def show_options(self):
        # Shows options to the user
        print("Choose your option: ")
        print("If you want to quit, enter 'quit'.")
        print("- Add two numbers")
        print("- Subtract two numbers")
        print("- Multiplicate two numbers")
        print("- Divide two numbers")

    def addition(self):
        # Addition function
        while True:
            try:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
                result = first_number + second_number
                print(f"Result is: {result}")
                if result:
                    self.show_options()
            except ValueError:
                print("Enter correct values!")

    def subtraction(self):
        # Subtraction function
        while True:
            try: 
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
                result = first_number - second_number
                print(f"Result is: {result}")
                if result:
                    self.show_options()
            except ValueError:
                print("Enter correct values!")

    def multiplication(self):
        # Multiplication function
        while True:
            try:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
                result = first_number * second_number
                print(f"Result is: {result}")
                if result:
                    self.show_options()
            except ValueError:
                print("Enter correct values!")

    def division(self):
        # Division function
        while True:
            try:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
                result = first_number / second_number
                print(f"Result is: {result}")
                if result:
                    self.show_options()
            except ZeroDivisionError:
                print("You can't divide by zero!")
            except ValueError:
                print("Enter correct values!")

    def quit_calculator(self):
        # Function to quit out from calculator
        print("Thanks for using our calculator!")

    def calculator_error(self):
        # Function to response user, if he entered wrong option
        print("You have entered option wrong! Check, if you have written words correctly...")
        print("For example: 'Basic calculator' (whitespaces are needed too). Try again!")

    def show_geometrical_options(self):
        # Shows options for geometrical calculator
        print("- Square area")
        print("- Square perimeter")
        print("- Rectangle area")
        print("- Rectangle perimeter")
        print("- Parallelogram area")
        print("- Parallelogram perimeter")
        print("- Trapezoid area")
        print("- Trapezoid perimeter")
        print("- Triangle area")
        print("- Triangle perimeter")
        print("- Circle area")
        print("- Circle circumference")

    def square_area(self):
        # Function to calculate square area
        while True:
            try:
                side = float(input("Enter a side: "))
                result = side ** 2
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct value!")

    def square_perimeter(self):
        # Function to calculate square perimeter
        while True:
            try:
                side = float(input("Enter a side: "))
                result = side * 4
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct value!")

    def rectangle_area(self):
        # Function to calculate rectangle area
        while True:
            try:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                result = length * width
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options() 
            except ValueError:
                print("Enter correct values!")

    def rectangle_perimeter(self):
        # Function to calculate rectangle perimeter
        while True:
            try:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                result = 2 * (length + width)
                print(f"Result is: {result}") 
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")

    def parallelogram_area(self):
        # Function to calculate parallelogram area
        while True:
            try:
                length = float(input("Enter length: "))
                height = float(input("Enter height: "))
                result = length * height
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")

    def parallelogram_perimeter(self):
        # Function to calculate parallelogram perimeter
        while True:
            try:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                result = (2 * length) + (2 * width)
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")

    def trapezoid_area(self):
        # Function to calculate trapezoid area
        while True:
            try:
                first_base = float(input("Enter first base: "))
                second_base = float(input("Enter second base: "))
                height = float(input("Enter height: "))
                result = (height * (first_base + second_base)) / 2
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")

    def trapezoid_perimeter(self):
        # Function to calculate trapezoid perimeter
        while True:
            try:
                first_side = float(input("Enter first side: "))
                second_side = float(input("Enter second side: "))
                first_base = float(input("Enter first base: "))
                second_base = float(input("Enter second base: "))
                result = first_side + second_side + first_base + second_base
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")

    def triangle_area(self):
        # Function to calculate triangle area
        while True:
            try:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                result = (base * height) / 2
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")

    def triangle_perimeter(self):
        # Function to calculate triangle perimeter
        while True:
            try:
                first_side = float(input("Enter first side: "))
                second_side = float(input("Enter second side: "))
                base = float(input("Enter base: "))
                result = first_side + second_side + base
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")

    def circle_area(self):
        # Function to calculate circle area
        while True:
            try:
                radius = float(input("Enter radius: "))
                result = math.pi() * radius ** 2
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")
    
    def circle_circumference(self):
        # Function to calculate circle circumference
        while True:
            try:
                radius = float(input("Enter radius: "))
                result = 2 * math.pi() * radius
                print(f"Result is: {result}")
                if result:
                    self.show_geometrical_options()
            except ValueError:
                print("Enter correct values!")
            
