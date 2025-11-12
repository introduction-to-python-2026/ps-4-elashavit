def split_before_each_uppercases(formula):
    start = 0
    splitted_formula = []
    for i in range(1, len(formula)):  # מתחילים מהתו השני
        if formula[i].isupper():
            splitted_formula.append(formula[start:i])
            start = i
    splitted_formula.append(formula[start:])
    return splitted_formula



def split_at_first_digit(formula):
    digit_location = len(formula)
    for i, ch in enumerate(formula):
        if ch.isdigit():
            digit_location = i
            break
    if digit_location == len(formula):
        return formula, 1
    prefix = formula[:digit_location]
    number_part = int(formula[digit_location:])
    return prefix, number_part
