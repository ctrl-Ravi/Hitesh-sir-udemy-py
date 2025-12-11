"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Update via name 
   - Delete via name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""


import csv
import os

FILENAME = 'contacts.csv'

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
      
def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
   
   # check for duplicate
    with open(FILENAME, "r", encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
          if row['Name'].lower()== name.lower():
              print("Contact name is  already exists")
              return
    with open(FILENAME,"+a",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name , phone, email])
        print("contact added")

def view_contacts():
    with open(FILENAME,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if len(rows) < 1:
            print("NO Contacts found.")
            return
        print("\n Your Contacts: \n")

        for row in rows:
            print(f"Name: {row['Name']} | Phone {row['Phone'] } | Email {row['Email']} \n ")
        print()

def search_contact():
    term = input("Enter the name to search : "). strip().lower()
    found = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader =csv.DictReader(f)
        for row in reader:
            if term in row['Name'].lower():
                print(f"{row['Name']} | {row['Phone']}")
                found = True
    if not found:
        print("Result not found")

def delete_contact():
   term = input("Enter the name to Delete : ").strip().lower()
   TempFILENAME='temp.csv'
   found = False

   with open(FILENAME, 'r', encoding="utf-8") as f, open(TempFILENAME, 'w', newline='',encoding="utf-8") as of:
        reader =csv.DictReader(f)
        writer= csv.writer(of)
        writer.writerow(["Name", "Phone", "Email"])
        for row in reader:
            if row and  row['Name'].lower()!= term:
                writer.writerow([row["Name"],row["Phone"],row["Email"]])
            elif term in row["Name"].lower():
                found = True
   os.remove(FILENAME)
   os.rename(TempFILENAME, FILENAME)
   if found:
     print(f"{term} Contact Deleted")
   else:
      print(f"{term} not found in the contact list")
      
def update_contact():
   term = input("Enter the name to Update : ").strip().lower()
   TempFILENAME='temp.csv'
   found = False

   with open(FILENAME, 'r', encoding="utf-8") as f, open(TempFILENAME, 'w', newline='',encoding="utf-8") as of:
        reader =csv.DictReader(f)
        writer= csv.writer(of)
        writer.writerow(["Name", "Phone", "Email"])
        for row in reader:
            if row and row["Name"].lower()!=term:
                writer.writerow([row["Name"],row["Email"],row["Phone"]]) # its take only one argument so write in list format
            elif row['Name'].lower()== term:
               phone = input("New Phone: ").strip()
               email = input("New Email: ").strip()
               writer.writerow([row["Name"],phone, email])
               found= True
         
   os.remove(FILENAME)
   os.rename(TempFILENAME, FILENAME)
   if found:
     print(f"{term} Contact Updated")
   else:
      print(f"{term} not found in the contact list")
                
                
    

def main():
    while True:
        print("\n 🫙Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        choice= input("Choose an option (1-4)").strip()
        if choice =='1':
            add_contact()
        elif choice== '2':
            view_contacts()
        elif choice== '3':
            search_contact()
        elif choice== '4':
            delete_contact()
        elif choice== '5':
            update_contact()
        elif choice== '6':
            print("Thanks for using our software")
            break
        else:
            print("Invalid Choice Please Choose Correct Option")

if __name__=="__main__":
    main()