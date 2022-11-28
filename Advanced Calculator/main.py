from Calculator import Calculator

while True:
    print("Hello! Welcome to calculator, which option you will choose?")
    print("If you want to quit, enter 'quit'.")
    answer = input("Basic calculator or Geometrical? Enter your answer: ")

    calculator = Calculator()

    if answer.lower() == 'quit':
        calculator.quit_calculator()
        break

    if answer.lower() == 'basic calculator':
        calculator.show_options()
        answer = input("Your answer: ")
        if answer.lower() == 'add two numbers':
            calculator.addition()
        elif answer.lower() == 'subtract two numbers':
            calculator.subtraction()
        elif answer.lower() == 'multiplicate two numbers':
            calculator.multiplication()
        elif answer.lower() == 'divide two numbers':
            calculator.division()
        elif answer.lower() == 'quit':
            calculator.quit_calculator()
            break

    if answer.lower() == 'geometrical calculator':
        calculator.show_geometrical_options()
        answer = input("Your answer: ")
        if answer.lower() == 'square area':
            calculator.square_area()
        elif answer.lower() == 'square perimeter':
            calculator.square_perimeter()
        elif answer.lower() == 'rectangle area':
            calculator.rectangle_area()
        elif answer.lower() == 'rectangle perimeter':
            calculator.rectangle_perimeter()
        elif answer.lower() == 'parallelogram area':
            calculator.parallelogram_area()
        elif answer.lower() == 'parallelogram perimeter':
            calculator.parallelogram_perimeter()
        elif answer.lower() == 'trapezoid area':
            calculator.trapezoid_area()
        elif answer.lower() == 'trapezoid perimeter':
            calculator.trapezoid_perimeter()
        elif answer.lower() == 'triangle area':
            calculator.triangle_area()
        elif answer.lower() == 'triangle perimeter':
            calculator.triangle_perimeter()
        elif answer.lower() == 'circle area':
            calculator.circle_area()
        elif answer.lower() == 'circle circumference':
            calculator.circle_circumference()
        elif answer.lower() == 'quit':
            calculator.quit_calculator()
            break
    else:
        calculator.calculator_error()
