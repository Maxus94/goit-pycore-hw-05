import re

def generator_numbers(text: str):
    # list = text.split()
    # print(list)    
    pattern = '[\d\.]+'
    result = re.findall(pattern, text) 
    print(result)
    return


generator_numbers('lk;lk l;k ;lk; l765.2k;iopi opi 122po 5 p;')