"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""


import base64
import os

VAULT_FILE= "vault.txt"
TEMP_FILE="temp.txt"
def encode(text):
    return base64.b64encode(text.encode()).decode() # .decode used to remove b b'cmF2aQ==' to only string 'cmF2aQ=='

def decode(text):
    return base64.b64decode(text.encode()).decode()


def password_strength(password):
    length=len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_special= any(c in "!@#$%^&*.,<>?" for c in password)

    score = sum([length >=8, has_upper, has_lower, has_special])
    return ["Weak", "Medium", "Strong", "Very strong"][min(score, 3)]



def add_credential():
    website = input("Website: ").strip()
    username= input("Username: ").strip()
    password= input("Password: ").strip()

    strength = password_strength(password)

    line = f"{website} || {username} || {password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, "a+", encoding="utf-8") as f:
        f.write(encoded_line + "\n")
        print("✔️ Credential Saved")
        print(strength)

def view_credential():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password="*" * len(password)
            print(f"{website} | {username} | {password}")
            # print(f"{website} | {username} | {hidden_password}")

def update_password():
    if not os.path.exists(VAULT_FILE):
        print("file not found")
    website_name= input("Enter website name which password you want to update: ").strip().lower()
    found=False
    with open(VAULT_FILE, 'r', encoding="utf-8") as f , open(TEMP_FILE,'+a',encoding="utf-8") as w:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            if website_name!=website.strip().lower():
                line = f"{website} || {username} || {password}"
                encoded_line = encode(line)
                w.write(encoded_line + "\n")
            elif website_name==website.strip().lower():
                new_pass=input("Enter Your new password: ")
                line = f"{website} || {username} || {new_pass}"
                encoded_line = encode(line)
                w.write(encoded_line + "\n")
                print("Password upadated")
                found = True
    if found:
        os.remove(VAULT_FILE)
        os.rename(TEMP_FILE,VAULT_FILE)

def delete_password():
    if not os.path.exists(VAULT_FILE):
        print("file not found")
    website_name= input("Enter website name which password you want to delete: ").strip().lower()
    found=False
    with open(VAULT_FILE, 'r', encoding="utf-8") as f , open(TEMP_FILE,'+a',encoding="utf-8") as w:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            if website_name!=website.strip().lower():
                line = f"{website} || {username} || {password}"
                encoded_line = encode(line)
                w.write(encoded_line + "\n")
            elif website_name==website.strip().lower():
                print(f"password data Data Deleted of {website_name}")
                found = True
    if found:
        os.remove(VAULT_FILE)
        os.rename(TEMP_FILE,VAULT_FILE)
            



def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credential")
        print("3. Update password")
        print("4. Delete password")
        print("5. Exit")

        choice= input("Choose your option (1-4): ")

        match choice:
            case "1": add_credential()
            case "2": view_credential()
            case "3": update_password()
            case "4": delete_password()
            case "5": break
            case _: print("invalid choice")

if __name__ == "__main__":
    main()