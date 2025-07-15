def vatCalculator(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print(vatCalculator(float(input())))
