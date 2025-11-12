def split_before_each_uppercases(formula):
   start = 0
   splitted_formula = []
   for i in range(len(formula)):
       if formula[i].isupper():
           splitted_formula.append(formula[start:i])
           start = i
   splitted_formula.append(formula[start:])
   return splitted_formula



def split_at_first_digit(formula):
    digit_location = 1

    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1
    
    if digit_location == len(formula):
        return formula, 1

    prefix = formula[:digit_location]
    number_part = int(formula[digit_location:])
    return prefix, number_part
