def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return " "    

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
            # return "Give me name and phone please."
    return inner

def show_contacts_error(func):
    def inner(*args, **kwargs):        
        try:            
            return func(*args, **kwargs)
        except ValueError as e:
            return e

    return inner

@input_error
def add_contact(args, contacts):    
    name, phone = args
    contacts[name] = phone
    return "Contact added."    
    
@input_error
def change_contact(args, contacts):
    name, phone = args        
    if contacts.get(name):
        contacts[name] = phone
    else: 
        raise ValueError("Contact doesn't exist") 
    return "Contact Updated."


def show_contact(args, contacts):
    name = args[0]    
    try:
        resp = contacts[name] 
        return resp
    except:
        raise ValueError("Contact doesn't exist") 

@show_contacts_error
def show_all(contacts):        
    resp = ""
    for contact in contacts:
        resp = resp + contact + " phone " + contacts[contact] + "\n"
    if resp == "":
        raise ValueError("There is no any contact")
    return resp
        

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()