import sys

def parse_command():
    return sys.argv        

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
            logs=[]            
            for line in file_content:
                line = line.strip()                
                line = line.replace(" ", "|", 3)
                line = line.split('|')                
                print({'date': line[0], 'time': line[1], 'level': line[2], 'text': line[3]})
    except:
        return "File not found or damaged"    
    return

def parse_log_line(line: str) -> dict:
    log_info = line.split(' ')

# print(parse_command())
print(load_logs(parse_command()[1]))