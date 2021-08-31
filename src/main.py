import json
def read_contacts():
	with open("contacts.json", "r") as f:
			contacts = json.loads(f.read())

			return contacts;
def write_contacts():
	samplejson = {"SampleContact": [{"number": "7148729143"}]}
	with open("contacts.json", "w") as f:
		json.dump(samplejson, f, indent=4)

def open_contacts():
	try:

		contacts = read_contacts()
	except FileNotFoundError:
		samplejson = {"SampleContact": [{"number": "7148729143"}]}
		write_contacts()
	

	return read_contacts();

def add_contact(name, number, filename='contacts.json'):
	with open(filename,'r+') as file:

		file_data = json.load(file)

		file_data[name] = [{
	"number": number,
}]
		file.seek(0)

		json.dump(file_data, file, indent = 4)


	return f"Done adding contact {name} with number {number}"

def delete_contact(name, filename="contacts.json"):
	with open(filename, "r") as file:

		data = json.load(file)
		try:

			data.pop(name)
		except KeyError:
			return f"No contact with the name {contact} exists." 

	with open(filename, "w") as file:
		json.dump(data, file, indent=4)

	return f"Done deleting contact {name}"

def showall(contacts):
	output = ""

	for i in contacts.items():
		name = i[0]
		info = i[1][0]
		number = info["number"]

		output += (f"\n{name}:( \n	number: {number}\n)")

	return output;

def show(contacts, contact):
	output = ""
	try:
		info = contacts[contact][0]

	except KeyError:
		return f"No contact with the name {contact} exists."

	number = info["number"]


	output = (f"\n{contact}: \n	number: {number}\n")

	return output;

def main():
	contacts = open_contacts()
	print("\ntype in 'help' for info\n")
	while True:
		choice = input()
		if choice in ["showall", "showall "]:
			print(showall(contacts))

		elif "show" in choice and choice.split(" ")[0] == "show":
			contact = choice[5:]
			print(show(contacts, contact))

		elif "insert" in choice:
			listofinfo = choice.split(" ")
			name = listofinfo[1]
			number = listofinfo[2]
			print(add_contact(name, number))

		elif "remove" in choice:
			listofinfo = choice.split(" ")
			name = "".join([listofinfo[1]])
			print(delete_contact(name))

		elif choice == "help":
			print("showall: shows all contacts\nshow (contactname): shows a specific contact\ninsert (contactname) (number): creates a new contact\nremove (contactname): removes the specified contact")

		else:
			print("Invalid command.")

		contacts = open_contacts()



main()