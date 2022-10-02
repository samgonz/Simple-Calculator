import calculate
import splashLogo

#Initial Splash Screen
print(splashLogo.logo)

#User inputs
first_number = float(input('What is the first number?\n'))
operator = input('What operator would you like to use?\n')
last_number = float(input('What is the last number?\n'))

#Result of the math operation
result = calculate.calculate(first_number, operator, last_number)

print(f'{first_number} {operator} {last_number} = {result}')