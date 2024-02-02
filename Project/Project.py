import sys
def main():
    while True:
        print("Please select your user type:")
        print("1. A public user")
        print("2. The owner of the keys")
        print("3. Exit program")
        user_type = input("Enter your choice: ")
       
        if user_type == "1":
            while True:
                print("As a public user, what would you like to do?")
                print("1. Send an encrypted message")
                print("2. Authenticate a digital signature")
                print("3. Exit")
                user_choice = input("Enter your choice: ")
               
                if user_choice == "1":
                    message = input("Enter a message: ")
                    print("Message encrypted and sent.")
                elif user_choice == "2":
                    print("There are no signatures to authenticate.")
                elif user_choice == "3":
                    sys.exit()
                else:
                    print("Invalid input. Please try again.")
       
        elif user_type == "2":
            while True:
                print("As the owner of the keys, what would you like to do?")
                print("1. Decrypt a received message")
                print("2. Digitally sign a message")
                print("3. Show the keys")
                print("4. Generating a new set of the keys")
                print("5. Exit")
                user_choice = input("Enter your choice: ")
               
                if user_choice == "1":
                    print("The following messages are available:")
                    print("1. (length = 9)")
                    Decrypted_message = input("Enter your choice: ")#No matter input which number here will print the decrypted message,maybe add else here to print invalid info
                    print("Decrypted message: TOPSECRET")#Should output according to the input
                elif user_choice == "2":
                    Signature = input("Enter a message: ")
                    print("Message signed and sent.")
                elif user_choice == "3":
                    print("Public Key: <public_key>")#public key
                    print("Private Key: <private_key>")#private key
                elif user_choice == "4":
                    print("New set of keys generated.")#New key
                elif user_choice == "5":
                    sys.exit()
                else:
                    print("Invalid input. Please try again.")
       
        elif user_type == "3":
            print("Bye for now!")
            sys.exit()
       
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()

