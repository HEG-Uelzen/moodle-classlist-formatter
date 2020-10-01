import os
import json
import string
from time import sleep
from pathlib import Path

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

    # email domain input
    e_domain = ("Please enter the E-Mail Domain of your students: ")
    sleep(10)
    
    for name in names:
        name_lowercase = name.lower()
        # print(name_lowercase)

        username = name_lowercase.replace(" ", ".")
        str(username)
        print(username)

        firstname = ""
        str(firstname)

        lastname = ""
        str(lastname)

        email = username + "@" + str(e_domain)
        str(email)
        print(email)

        final_line = username + ";" + password + ";" + firstname + ";" + lastname + ";" + email

        final.append(final_line)


        

    
if __name__ == "__main__":
    main()