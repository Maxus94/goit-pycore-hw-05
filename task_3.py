import sys

def parse_command():
    return sys.argv        

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
    except:
        return "File not found or damaged"    
    return file_content

def parse_log_line(line: str) -> dict:
    pass

# print(parse_command())
print(load_logs(parse_command()[1]))