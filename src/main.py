import json
import jsonpickle



def read_contacts():
    with open("contacts.json", "r") as f:
            contacts = json.loads(f.read())

            return contacts;




def get_contact_info(contact, specific=False):
    if not specific:

        info = contact[1][0]
    else:
        info = contact
    number = info["number"]
    email = info["email"]
    note = info["additional info"]

    return [number, email, note]



def write_contacts():
    samplejson = {"SampleContact": [{"number": "7148729143", "email": "email@email.com", "additional info": "note"}]}
    with open("contacts.json", "w") as f:
        json.dump(samplejson, f, indent=4)




def open_contacts():
    try:

        contacts = read_contacts()
    except FileNotFoundError:
        write_contacts()
    

    return read_contacts();




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
            return f"No contact with the name {contact} exists.\n" 

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    return f"Done deleting contact {name}\n"




def show(contacts, contact=None):
    output = ""
    index = 0
    if contact == None:
        for contact in contacts:
            for contactinfo in contacts.items():
                name = contact
                listofinfo = get_contact_info(contactinfo)
                if name not in output:

                    output += (f"\n{name}:( \n  number: {listofinfo[0]}\n  email: {listofinfo[1]}\n  additional info: {listofinfo[2]}\n)\n\n")
    else:
        try:
            info = contacts[contact][0]
        except KeyError:
            return "no contact with the name {contact} exists."
        name = contact
        listofinfo = get_contact_info(info, True)
        output = (f"\n{name}:( \n  number: {listofinfo[0]}\n  email: {listofinfo[1]}\n  additional info: {listofinfo[2]}\n)\n\n")


    return output;




def insert(choice):
    number, email, note = "unknown", "unknown", "unknown"
    listofinfo = choice.split(" ")
    listofinfo = [x for x in listofinfo if x != ""]
    try:
        name = listofinfo[1]
    except IndexError:
        return False
    try:
        number = listofinfo[2]
        email = listofinfo[3]
        note = listofinfo[4]
    except IndexError:
        pass

    return name, number, email, note




def main():
    contacts = open_contacts()
    print("\ntype in 'help' for info\n")
    while True:
        choice = input()
        if choice in ["showall", "showall "]:
            print(show(contacts))

        elif "show" in choice and choice.split(" ")[0] == "show":
            contact = choice[5:]
            print(show(contacts, contact))

        elif "insert" in choice:
            try:

                name, number, email, note = insert(choice)
                print(add_contact(name, number, email, note))
            except TypeError:
                print("insert requires an argument")
                continue
            
        elif "remove" in choice:
            listofinfo = choice.split(" ")
            name = "".join([listofinfo[1]])
            print(delete_contact(name))

        elif choice == "help":
            print("\nshowall: shows all contacts\nshow (contactname): shows a specific contact\ninsert (contactname), optional(number), optional(email), optional(note): creates a new contact or updates an existing one\nremove (contactname): removes the specified contact\n\n")

        else:
            print("Invalid command.\n\n")

        contacts = open_contacts()



main()