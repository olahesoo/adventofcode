def calculate(name, monkey_equations):
    equation = monkey_equations[name]
    if type(equation) == int:
        return equation

    first_result = calculate(equation[0], monkey_equations)
    second_result = calculate(equation[2], monkey_equations)
    if equation[1] == '+':
        result = first_result + second_result
    if equation[1] == '-':
        result = first_result - second_result
    if equation[1] == '*':
        result = first_result * second_result
    if equation[1] == '/':
        result = int(first_result / second_result)
    monkey_equations[name] = result
    return result

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

monkey_equations = {}

for i in inlines:
    monkey_math = i.split(' ')
    name = monkey_math[0][:-1]
    if len(monkey_math) == 2:
        monkey_equations[name] = int(monkey_math[1])
    else:
        assert len(monkey_math) == 4
        monkey_equations[name] = monkey_math[1:]

print(calculate('root', monkey_equations))

