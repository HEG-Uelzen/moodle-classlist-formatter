import os
import json
import string
import platform

from time import sleep
from pathlib import Path

def main():
    # file_url = input("Enter the direction of your JSON-file: ")
    current = str(Path.cwd().absolute())
    
    if platform.system() == "Windows":
        file_url = current + "\\names.json"

    else:
        file_url = current + "/names.json"

    print("--------")
    print("Programm is starting")
    print("--------")

    final = []

    # read file 
    names = json.loads(open(file_url).read())
    # print(names)

    # password input
    password = input("Please enter the default password for your students: ")
    password = str(password)
    print("You set " + password + " as default password.")

    # email domain input
    e_domain = input("Please enter the E-Mail Domain of your students: ")
    print("You set " + e_domain + " as your studendts e-mail domain.")
    
    print()
    print("------")
    print()
    sleep(4)

    for name in names:
        name_lowercase = name.lower()
        # print(name_lowercase)

        username = name_lowercase.replace(" ", ".")
        username = str(username)
        # print(username)

        vornachname = name.split(' ')

        firstname = vornachname[0]
        firstname = str(firstname)

        lastname = vornachname[1]
        lastname = str(lastname)

        email = username + "@" + e_domain
        email = str(email)
        # print(email)

        final_line = username + ";" + password + ";" + firstname + ";" + lastname + ";" + email
        print(final_line)

        final.append(final_line)

    print()
    print("Creating output file...")
    print()
    sleep(1)

    output_file = open("output.txt", "w+")

    for item in final:
        output_file.write(item + '\n')


        

    
if __name__ == "__main__":
    main()