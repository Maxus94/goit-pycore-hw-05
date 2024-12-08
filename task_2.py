import re
from decimal import Decimal

def generator_numbers(text: str):        
    """
    Take numbers from string angive it one by one by demand
    """
    pattern = '\d+\.\d+'
    numbers = re.findall(pattern, text)    
    for number in numbers:
        yield(number)

def sum_profit(text: str, generator_numbers):
    """
    Calculate numbers were given by generator_numbers function
    """
    sum = '0'
    for number in generator_numbers(text):
        sum = Decimal(sum) + Decimal(number)
    return sum


total_income = sum_profit("", generator_numbers)

# total_income = sum_profit("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.", generator_numbers)

print(f"Загальний дохід: {total_income}")