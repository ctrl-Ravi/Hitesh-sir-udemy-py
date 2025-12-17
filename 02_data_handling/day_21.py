"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""


import os
import json
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE= "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key= Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key =f.read()
    return Fernet(key)

fernet= load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save_vault(data):
    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_note():
    title=input("Enter note title: ").strip()
    content=input("Enter note content: ").strip()
    
    encrpted_content=fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    data= load_vault()
    data.append({
        "title": title,
        "content" : encrpted_content,
        "timestamp": timestamp
    })

    save_vault(data)
    print("✔️ data saved")

def list_notes():
    data= load_vault()
    if not data:
        print("No NOtes yet")
        return

    for i, note in enumerate(data,1):
        print(f"{i}. {note['title']} {note['timestamp']}")

def view_note():
    list_notes()
    try:
        index=int(input("Enter Note number to view: ")) -1
        data= load_vault()
        if 0<= index <= len(data):
            encrypted=data[index]["content"]
            decrypted=fernet.decrypt(encrypted.encode()).decode()
            print(f"📝 {data[index]['title']} - {data[index]['timestamp']} \n Content \n {decrypted}")
        else:
            print("Invalid selection")
    except Exception as e:
        print(f"Invalid input {e}")

def search_note():
    note_name= input("Enter notes title name: ").strip().lower()
    data= load_vault()

    # found = False
    # for i, note in enumerate(data):    
    #     if note_name==note['title'].lower():
    #         index =i
    #         encrypted = data[index]['content']
    #         decrypted =fernet.decrypt(encrypted.encode()).decode()
    #         print(f"📝 {data[index]['title']} - {data[index]['timestamp']} \n Content \n {decrypted}")
    #         found = True
    # if not found:
    #     print("Title not availble in the Notes")


    found = [note for note in data if note_name in note["title"].lower()]
    if not found:
        print("No Matching notes")
    else:
        for note in found:
            print(f"{note['title']} - {note["timestamp"]} ")

def main():       
    while True:
        print("📝Offline Notes locker")
        password = input("Please Enter your password to unlock the vault: ").strip().lower()
        if password=="ravi":
            print("1. Add notes")
            print("2. view notes")
            print("3. list notes")
            print("4. Search notes")
            print("5. Exit")

            choice = input("Enter Your Choice: ").strip()

            match choice:
                case "1": add_note()
                case "2": view_note()
                case "3": list_notes()
                case "4": search_note()
                case "5": break
                case _: print("invalid choice")
        else:
            print("Please Enter correct password")
            continue

if __name__ == "__main__":
    main()