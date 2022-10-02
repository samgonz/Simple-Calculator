from tokenize import String
import calculate
import splashLogo

continue_math = ''

#Initial Splash Screen
print(splashLogo.logo)

#User inputs
first_number = float(input('What is the first number?\n'))
operator = input('What operator would you like to use?\n')
next_number = float(input('What is the next number?\n'))
result = calculate.calculate(first_number, operator, next_number)
print(f'{first_number} {operator} {next_number} = {result}\n')

while continue_math.lower() != 'n':
    #Result of the math operation

    continue_math = input('Would you like to enter another number? [Y or N]\n')
    
    if continue_math.lower() != 'n':
        operator = input('What operator would you like to use?\n')
        next_number = float(input('What is the next number?\n'))
    elif continue_math.lower() == 'n':
        print(f'{f_number} {operator} {next_number} = {result}\n')
        break
    
    f_number = result
    result = calculate.calculate(f_number, operator, next_number)
    print(f'{f_number} {operator} {next_number} = {result}\n')  