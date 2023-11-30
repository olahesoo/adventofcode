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

has_human_buffer = {}
def has_human(name, monkey_equations):
    if name in has_human_buffer:
        return has_human_buffer[name]
    if name == 'humn':
        return True
    equation = monkey_equations[name]
    if type(equation) == int:
        return False
    result = has_human(equation[0], monkey_equations) or has_human(equation[2], monkey_equations)
    has_human_buffer[name] = result
    return result

def get_match_function(name, monkey_equations, current_function=None):
    equation = monkey_equations[name]
    left = equation[0]
    operator = equation[1]
    right = equation[2]
    if left == 'humn' or has_human(left, monkey_equations):
        right = calculate(right, monkey_equations)
        if left == 'humn':
            if operator == '+':
                if not current_function:
                    return lambda x: x - right
                return lambda x: current_function(x) - right
            if operator == '-':
                if not current_function:
                    return lambda x: x + right
                return lambda x: current_function(x) + right
            if operator == '*':
                if not current_function:
                    return lambda x: int(x - right)
                return lambda x: int(current_function(x) / right)
            if operator == '/':
                if not current_function:
                    return lambda x: x * right
                return lambda x: current_function(x) * right
        else:
            if operator == '+':
                if not current_function:
                    return get_match_function(left, monkey_equations, lambda x: x - right)
                return get_match_function(left, monkey_equations, lambda x: current_function(x) - right)
            if operator == '-':
                if not current_function:
                    return get_match_function(left, monkey_equations, lambda x: x + right)
                return get_match_function(left, monkey_equations, lambda x: current_function(x) + right)
            if operator == '*':
                if not current_function:
                    return get_match_function(left, monkey_equations, lambda x: int(x / right))
                return get_match_function(left, monkey_equations, lambda x: int(current_function(x) / right))
            if operator == '/':
                if not current_function:
                    return get_match_function(left, monkey_equations, lambda x: x * right)
                return get_match_function(left, monkey_equations, lambda x: current_function(x) * right)
    
    left = calculate(left, monkey_equations)
    if right == 'humn':
        if operator == '+':
            if not current_function:
                return lambda x: x - left
            return lambda x: current_function(x) - left
        if operator == '-':
            if not current_function:
                return lambda x: left - x
            return lambda x: left - current_function(x)
        if operator == '*':
            if not current_function:
                return lambda x: int(x / left)
            return lambda x: int(current_function(x) / left)
            if not current_function:
                return lambda x: int(left / x)
        if operator == '/':
            if not current_function:
                return lambda x: int(left / x)
            return lambda x: int(left / current_function(x))

    if operator == '+':
        if not current_function:
            return get_match_function(right, monkey_equations, lambda x: x - left)
        return get_match_function(right, monkey_equations, lambda x: current_function(x) - left)
    if operator == '-':
        if not current_function:
            return get_match_function(right, monkey_equations, lambda x: left - x)
        return get_match_function(right, monkey_equations, lambda x: left - current_function(x))
    if operator == '*':
        if not current_function:
            return get_match_function(right, monkey_equations, lambda x: int(x / left))
        return get_match_function(right, monkey_equations, lambda x: int(current_function(x) / left))
    if operator == '/':
        if not current_function:
            return get_match_function(right, monkey_equations, lambda x: int(left / x))
        return get_match_function(right, monkey_equations, lambda x: int(left / current_function(x)))

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

monkey_equations['humn'] = None

root = monkey_equations['root']
if has_human(root[0], monkey_equations):
    match_function = get_match_function(root[0], monkey_equations)
    right_side = calculate(root[2], monkey_equations)
    result =  match_function(right_side)
else:
    match_function = get_match_function(root[2], monkey_equations)
    left_side = calculate(root[0], monkey_equations)
    result =  match_function(left_side)

print(result)

