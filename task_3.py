import sys, collections

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
            logs=[]            
            for line in file_content:
                line = line.strip()                
                logs.append(parse_log_line(line))
    except:
        return "File not found or damaged"    
    return logs

def parse_log_line(line: str) -> dict:
    line = line.replace(" ", "|", 3)
    line = line.split('|')                
    return {'date': line[0], 'time': line[1], 'level': line[2], 'text': line[3]}

def filter_logs_by_level(logs: list, level: str) -> list:
    log_level=filter(lambda log: log['level'] == level, logs)
    return list(log_level)

def count_logs_by_level(logs: list) -> dict:
    levels = []
    for item in logs:
        levels.append(item['level'])        
    level_counts = dict(collections.Counter(levels))    
    return level_counts    

def display_log_counts(counts: dict):
    counts_header = f"{'Рівень логування':<17}{'| '}{'Кількість':<10}"    
    print(f"\n{counts_header}")
    print('-'*16, "|", '-'*9)        
    for key in counts:
        print(f"{key:<17}{'| '}{counts[key]:<10}")
    return

display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))
if len(sys.argv) == 3:    
    logs = filter_logs_by_level(load_logs(sys.argv[1]), sys.argv[2])    
    print(f"\nДеталі логів для рівня '{sys.argv[2]}':")
    for log in logs:        
        print(f"{log['date']} {log['time']} - {log['text']}")