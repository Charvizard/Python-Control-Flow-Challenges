def large_power(base, exponent):
    if (base**exponent > 5000) : 
        return True
    else :
        return False

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent) : 
    if (budget < (food_bill + electricity_bill + internet_bill + rent)) : 
        return True
    else : 
        return False

def twice_as_large(num1, num2) : 
    if (num1 > num2*2) : 
        return True
    else:
        return False

def divisible_by_ten(num) : 
    if (num%10 == 0) : 
        return True
    else : 
        return False

def not_sum_to_ten(num1, num2) : 
    if ((num1 + num2) == 10) : 
        return False
    else : 
        return True