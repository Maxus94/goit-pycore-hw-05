import sys, collections, re
from pathlib import Path
from datetime import datetime

file = "text.log"
log_file = "text.log"
log_lvl = "ERROR"

def load_logs(file_path: str) -> list:
    """
    Create list of log records from log file
    """    
    p = Path(file_path)
    if not p.exists():        
        # raise FileNotFoundError(f"File {sys.argv[1]} not found")
        raise FileNotFoundError(f"File not found")
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.readlines()
        logs=[]            
        for line in file_content:
            line = line.strip()                            
            logs.append(parse_log_line(line))                                       
    return logs

def parse_log_line(line: str) -> dict:
    """
    Convert log record to dictionary of it's properties
    """    
    line = line.replace(" ", "|", 3)
    line = line.split('|')
    # print(len(line)!=4)
    if len(line) != 4:        
        # raise TypeError(f"File of logs {sys.argv[1]} has wrong format")        
        raise TypeError(f"File of logs has wrong format")        
    return {'date': line[0], 'time': line[1], 'level': line[2].upper(), 'text': line[3]}

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Select log records by name of level from list of all log records
    """    
    log_level=filter(lambda log: log['level'] == level.upper(), logs)
    return list(log_level)

def count_logs_by_level(logs: list) -> dict:
    """
    Create dictionary of log levels {level: number of log records of this level} from list of all log records
    """    
    global levels
    for item in logs:
        levels.append(item['level'])        
    level_counts = dict(collections.Counter(levels))    
    return level_counts    

def display_log_counts(counts: dict):
    """
    Print number of log records of each level in log file
    """    
    counts_header = f"{'Рівень логування':<17}{'| '}{'Кількість':<10}"    
    print(f"\n{counts_header}")
    print('-'*16, "|", '-'*9)        
    for key in counts:
        print(f"{key:<17}{'| '}{counts[key]:<10}")
    return

levels = []
# logs_list = load_logs(sys.argv[1])
logs_list = load_logs(file)

display_log_counts(count_logs_by_level(logs_list))
# if len(sys.argv) == 3:
if len(log_file) != 0:
    """
    Print all log records of level if second parameter of command line is exist
    """    
    # if sys.argv[2].upper() not in set(levels):
    if log_lvl.upper() not in set(levels):
        print(f"\nЛоги не знайдено, у файлі є такі рівні: {set(levels)}")
        # print(f"\nЛоги для рівня '{sys.argv[2].upper()}' не знайдено, у файлі {sys.argv[1]} є такі рівні: {set(levels)}")
    else:
        logs = filter_logs_by_level(logs_list, log_lvl)
        # logs = filter_logs_by_level(logs_list, sys.argv[2])            
        # print(f"\nДеталі логів для рівня '{sys.argv[2].upper()}':")
        print(f"\nДеталі логів:")
        for log in logs:        
            print(f"{log['date']} {log['time']} - {log['text']}")