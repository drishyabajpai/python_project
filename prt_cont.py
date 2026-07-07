contact={}


def add_contact():
    name=input("Enter Name: ")
    phone=input("Enter Phone Number: ")
    contact[name]=phone # store the name and phone number in the contact dictionary with the name as the key and phone number as the value
    print("Contact Added Successfully!")

def view_contacts():
    if not contact: # check if the contact dictionary is empty
        print("No Contacts Found.")
        return

    print("\n========== CONTACT LIST ==========")
    for name, phone in contact.items(): # iterate through the contact dictionary and print the name and phone number of each contact
        print(f"Name: {name}, Phone: {phone}")

def search_contact():
    name=input("Enter Name: ")
    if name in contact: # check if the name exists in the contact dictionary
        print(f"Contact Found: Name: {name}, Phone: {contact[name]}") # print the name and phone number of the contact if found
    else:
        print("Contact Not Found.")

def delete_contact():
    name=input("Enter Name:")
    if name in contact: # check if the name exists in the contact dictionary
        del contact[name] # delete the contact from the dictionary if found
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found.")

def update_contact():
    name=input("Enter Name:")
    if name in contact: # check if the name exists in the contact dictionary
        phone=input("Enter New Phone Number:") # prompt the user to enter a new phone number
        contact[name]=phone # update the phone number of the contact in the dictionary
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found.")

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")   
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")  
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
      
    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts() 

    elif choice == "3":
        search_contact()
    
    elif choice == "4":
        delete_contact()    

    elif choice == "5":
        update_contact() 
    
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
 

print("Thank you for using the Contact Book!") 