import os

current_user = os.getlogin()

def find_current_state():
    filename = 'C:\\Users\\'+current_user+'\\AppData\\Roaming\\Microsoft\\Teams\\logs.txt'
    path = os.path.join(os.getcwd(), filename)
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            if "current state:" in line:
                current_state = line.split("->")[1].split(")")[0].strip()
                return current_state
        return None
    
status = find_current_state()

print (status)