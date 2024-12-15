def get_tax(x):
    limits = [300000, 700000, 1000000, 1200000, 1500000]
    rates = [0, 0.05, 0.1, 0.15, 0.2, 0.3]
    tax = 0
    prev_limit = 0

    for i in range(len(limits)):
        if x > limits[i]:
            taxable_income = limits[i] - prev_limit
            tax += taxable_income * rates[i]
            prev_limit = limits[i]
        else:
            taxable_income = x - prev_limit
            tax += taxable_income * rates[i]
            break

    if x > limits[-1]:
        tax += (x - limits[-1]) * rates[-1]

    return tax