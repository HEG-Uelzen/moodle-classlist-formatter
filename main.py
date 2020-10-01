import os
import json
import string
from time import sleep
# from pathlib import Path

def main():
    # file_url = input("Enter the direction of your JSON-file: ")

    print("--------")
    print("Programm is starting")
    print("--------")

    final = []

    # read file 
    names = json.loads(open("/home/codespace/workspace/moodle-classlist-formatter/names.json").read())
    # print(names)

    # password input
    password = input("Please enter the default password for your students: ")
    # password = str(password)
    print("You set " + password + " as default password.")

    # email domain input
    e_domain = input("Please enter the E-Mail Domain of your students: ")
    print("You set " + e_domain + " as your studendts e-mail domain.")
    
    for name in names:
        name_lowercase = name.lower()
        # print(name_lowercase)

        username = name_lowercase.replace(" ", ".")
        username = str(username)
        print(username)

        firstname = ""
        firstname = str(firstname)

        lastname = ""
        lastname = str(lastname)

        email = username + "@" + e_domain
        email = str(email)
        print(email)

        final_line = username + ";" + password + ";" + firstname + ";" + lastname + ";" + email
        print(final_line)

        final.append(final_line)


        

    
if __name__ == "__main__":
    main()