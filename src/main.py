
import json




def read_contacts():
    with open("contacts.json", "r") as f:
            contacts = json.loads(f.read())

            return contacts;



def write_contacts():
    samplejson = {"SampleContact": [{"number": "7148729143", "email": "email@email.com", "additional info": "note"}]}
    with open("contacts.json", "w") as f:
        json.dump(samplejson, f, indent=4)

    open_contacts()




def open_contacts():
    try:

        contacts = read_contacts()
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        write_contacts()
        contacts = read_contacts() #tried calling open_contacts() again here but didn't work so i had to repeat myself.

    return contacts;
    




def add_contact(name, number, email, note):
    with open("contacts.json",'r') as file:

        file_data = json.load(file)

        file_data[name] = [{
    "number": number,
    "email": email,
    "additional info": note
}]
        file.seek(0)

    with open("contacts.json","w") as file:
        json.dump(file_data, file, indent = 4)


    return f"Done adding/updating contact {name}\n"



def delete_contact(name, filename="contacts.json"):
    with open(filename, "r") as file:

        data = json.load(file)
        try:

            data.pop(name)
        except KeyError:
            return False

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    return True;



def dict_to_individual_vars(info): #another best name function
    name, number, email, note = info["name"], info["number"], info["email"], info["note"]

    return name, number, email, note



def prettyprintinfo(dictofinfo):
    name, number, email, note = dictofinfo["name"], dictofinfo["number"], dictofinfo["email"], dictofinfo["note"]
    output = f"\n{name}:\n\n     number: {number}\n     email: {email}\n     additional info: {note}"

    return output;



def show(contacts, contact=None):
    try:
        info = contacts[contact][0]
    except KeyError:
        return False
    name, number, email, note = contact, info["number"], info["email"], info["additional info"]

    dictofinfo = {"name": name, "number": number, "email": email, "note": note}

    return prettyprintinfo(dictofinfo)



def showall(contacts):
    output = """"""
    for contact in contacts:
        output += show(contacts, contact)

    return output;




def extract_info_from_user_input(choice): #best function name
    number, email, note = "unknown", "unknown", "unknown"
    listofinfo = choice.split(" ")
    listofinfo = [x for x in listofinfo if x != ""]
    if len(listofinfo) > 5 or len(listofinfo) == 1:
        return False
    name = listofinfo[1]
    try:
        number = listofinfo[2]
        email = listofinfo[3]
        note = listofinfo[4]
    except IndexError:
        pass

    return {"name": name, "number": number, "email": email, "note": note}



def print_help():
    print("\nshowall: shows all contacts\nshow (contactname): shows a specific contact\ninsert (contactname), optional(number), optional(email), optional(note): creates a new contact or updates an existing one\nremove (contactname): removes the specified contact\n\n")



def check_command(choice, contacts):
    choicelist = choice.split(" ")
    match choicelist[0]:
        case "insert":
            Command.Insert(choice)
        case "remove":
            Command.remove(choice)
        case "show":
            Command.show(choice, contacts)
        case "help":
            Command.help()
        case "showall":
            Command.showallcmd(contacts)
        case _:
            print("\nInvalid Command.")

def main():
    print("\ntype in 'help' for info\n")
    while True:
        contacts = open_contacts()
        choice = input()
        check_command(choice, contacts)


class Command:
    def showallcmd(contacts):
        print(showall(contacts))
    def help():
        print("\nshowall: shows all contacts\nshow (contactname): shows a specific contact\ninsert (contactname), optional(number), optional(email), optional(note): creates a new contact or updates an existing one\nremove (contactname): removes the specified contact\n\n")
    def Insert(choice):
        info = extract_info_from_user_input(choice)
        if info != False:

            name, number, email, note = dict_to_individual_vars(info)
            print(add_contact(name, number, email, note))
        else:
            print("Insert takes from 1 to 4 arguments\n")

    def show(choice, contacts):
        try:
            choicelist = choice.split(" ")
            print(choicelist)
            contact = choicelist[1]
            worked = show(contacts, contact)
            if worked == False:
                print(f"No contact with the name {contact} exists.")
            else:
                print(worked)
        except IndexError:
            print("show requires an argument")

    def remove(choice):
        listofinfo = choice.split(" ")
        try:

            name = "".join([listofinfo[1]])
            worked = delete_contact(name)
            if worked == True:
                print(f"Done deleting contact {name}\n")
            else:
                print(f"No contact called {name} exists")
        except IndexError:
            print("remove requires an argument\n")

        


main()