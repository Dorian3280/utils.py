import re

def get_variable_from_equation(s):
    s = s.replace(' ', '')
    max_exponent = int(max(re.findall('(?<=\^)\d+', s)))
    part_of_regex = '|'.join([f'''([+-]?\\d+(?=x\^{i}))''' for i in range(1, max_exponent + 1)])
    regex = re.compile(f'((?:(?<=[^^])|^)[+-]?\d+(?:(?=[+-])|$))|{part_of_regex}')
    matches = re.findall(regex, s)
    # 1st step: Convert all values into int or 0 if they are empty
    # 2e step: Zip all tuples and sum them
    # 3e step : Convert the result to tuple
    return tuple(map(sum, zip(*map(lambda x: map(lambda x: int(x) if x != '' else 0, x), matches))))
    # return variables in a dynamic form as shown : (constant, x^1 variable, x^2 variable, and so on...)