import os
import json
import string
import platform

from time import sleep
from pathlib import Path
from progress.bar import Bar
from progress.spinner import Spinner


def main():
    # file_url = input("Enter the direction of your JSON-file: ")
    
    # find names.json file
    current = str(Path.cwd().absolute())
    
    # os detection for correct names file direction syntax
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
    sleep(1)

    bar = Bar("Processing", max=len(names))

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
        # print(final_line)

        final.append(final_line)

        bar.next()
        sleep(0.1)

    bar.finish()

    print()
    print("Creating output file...")
    print()
    sleep(1)

    output_file = open("output.txt", "w+")

    spinner = Spinner("Writing...")

    for item in final:
        output_file.write(item + '\n')
        spinner.next()
        sleep(0.1)

    spinner.finish()

        

    
if __name__ == "__main__":
    main()