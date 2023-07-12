# The code starts with importing necessary modules, random and string, 
# which are used for generating random passwords and working with string operations, respectively.
import random
import string

# The generate_password function is defined. This function takes in parameters for the desired length of the password, 
# and whether to include digits and symbols in the generated password. 
# It generates a password by selecting random characters from the available
def generate_password(length=8, include_digits=True, include_symbols=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# The main function is defined as the entry point of the program. 
# It prompts the user for input regarding the desired length of the password, 
# whether to include digits and symbols, and the number of passwords to generate.
def main():
    print("Welcome to the Password Generator App!")
    length = int(input("Enter the desired length of your password: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    num_passwords = int(input("How many passwords would you like to generate? "))

#Inside the main function, a list called passwords is initialized to store the generated passwords.
    passwords = []
# A loop is used to generate the requested number of passwords. 
# For each iteration, the generate_password function is called with the provided parameters, 
# and the generated password is appended to the passwords list.
    for _ in range(num_passwords):
        password = generate_password(length, include_digits, include_symbols)
        passwords.append(password)

# The generated passwords are then displayed to the user.
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

# The user is prompted to determine whether they want to save the passwords to a file. 
    save_to_file = input("\nWould you like to save the passwords to a file? (y/n): ").lower() == 'y'
# If they choose to do so, they are asked to enter a filename.
    if save_to_file:
        filename = input("Enter the filename to save the passwords: ")
# If the user opts to save the passwords, a file is opened in write mode using the provided filename. 
        with open(filename, 'w') as file:
# The writelines method is used to write each password from the passwords list to the file, with each password on a new line.
            file.writelines(password + '\n' for password in passwords)
# Finally, a confirmation message is displayed to indicate that the passwords have been saved to the file.
        print("Passwords saved to", filename)

# The code concludes by checking if the script is being run directly (not imported) and if so, 
# it calls the main function to start the program.
if __name__ == '__main__':
    main()
