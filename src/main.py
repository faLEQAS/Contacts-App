
import json




def read_contacts():
    try:

        with open("contacts.json", "r") as f:
                contacts = json.loads(f.read())

                return contacts;
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        write_contacts()
        contacts = read_contacts()

    return contacts;


def write_contacts():
    samplejson = {"SampleContact": [{"number": "7148729143", "email": "email@email.com", "additional info": "note"}]}
    with open("contacts.json", "w") as f:
        json.dump(samplejson, f, indent=4)

    open_contacts()
    




def add_contact(info):
    with open("contacts.json",'r') as file:

        file_data = json.load(file)

        for contactinfo in info:


            name, number, email, note = contactinfo["name"], contactinfo["number"], contactinfo["email"], contactinfo["note"]

            file_data[name] = [{
        "number": number,
        "email": email,
        "additional info": note
    }]
            file.seek(0)

    with open("contacts.json","w") as file:
        json.dump(file_data, file, indent = 4)



def delete_contact(names, filename="contacts.json"):
    with open(filename, "r") as file:
        data = json.load(file)
        for name in names:

            try:

                data.pop(name)
            except KeyError:
                return False

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    return True;



def prettyprintinfo(dictofinfo):
    name, number, email, note = dictofinfo["name"], dictofinfo["number"], dictofinfo["email"], dictofinfo["note"]
    output = f"\n{name}:\n\n     number: {number}\n     email: {email}\n     additional info: {note}"

    return output;



def show(contacts, contactlist=None):
    output = ""
    for contact in contactlist:
        if contact in [" ", ""]:
            continue
        try:
            info = contacts[contact][0]
        except KeyError:
            return False
        name, number, email, note = contact, info["number"], info["email"], info["additional info"]

        dictofinfo = {"name": name, "number": number, "email": email, "note": note}

        output += prettyprintinfo(dictofinfo)

    return output



def showall(contacts):
    contactlist = []
    for contact in contacts:
        contactlist.append(contact)

    output = show(contacts, contactlist)
    return output;




def extract_info_from_user_input(choice): #best function name
    listofinfo = choice.split(",")
    listofcontact = []
    for i in listofinfo:
        number, email, note = "unknown", "unknown", "unknown"
        i = i.split(" ")
        i = [x for x in i if x not in ["", " ", "insert"]]
        try:
            name = i[0]
        except IndexError:
            return False
        try:
            number = i[1]
            email = i[2]
            note = i[3]
        except IndexError:
            pass

        listofcontact.append(({"name": name, "number": number, "email": email, "note": note}))

    return listofcontact;



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
        contacts = read_contacts()
        choice = input()
        check_command(choice, contacts)


class Command:
    def showallcmd(contacts):
        print(showall(contacts))
    def help():
        print("\nshowall: shows all contacts\nshow (contact1) (contact2)...: shows only specified contacts\ninsert (contactname), optional(number), optional(email), optional(note): creates a new contact or updates an existing one\nremove (contactname): removes the specified contact\n\n")
    def Insert(choice):
        info = extract_info_from_user_input(choice)
        if info != False:
            add_contact(info)
            print(f"done adding/updating contact")
        else:
            print("Insert requires at least 1 argument\n")

    def show(choice, contacts):

        choicelist = choice.split(" ")
        contactlist = [x for x in choicelist[1:] if x not in ["", " "]]
        if contactlist == []:
            print("show requires at least 1 argument")
            return
        worked = show(contacts, contactlist)
        if not worked:
            print(f"One or more of the contacts you specified don't exist.")
            return
        print(worked)


    def remove(choice):
        listofinfo = choice.split(" ")

        names = [i for i in listofinfo[1:] if i not in ["", " "]]
        if names == []:
            print("remove requires at least 1 argument")
            return
        worked = delete_contact(names)
        if worked:
            print(f"Done deleting contacts\n")
            return

        print(f"One or more of the contacts you specified don't exist.")


        
if __name__ == "__main__":


    main()