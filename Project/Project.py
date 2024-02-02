from RSA import RSA

def main():
    rsa_instance = RSA(1024)  # Initialize RSA instance

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
                    encrypted_msg = rsa_instance.encrypt(message)
                    rsa_instance.newFile(encrypted_msg)
                    print("Message encrypted and sent")
                elif user_choice == "2":
                    signatures = rsa_instance.getFiles("signatures")
                    if len(signatures) == 0:
                        print("No signatures available to authenticate.")
                        continue

                        # THIS NEEDS WORK
                    print("The following messages are available:")
                    for i in range(len(signatures)):
                        print(str(signatures[i]))
                    message_number = int(input("Enter your choice: "))
                    print("Signature authenticated")
                elif user_choice == "3":
                    break
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
                    messages = rsa_instance.getFiles()
                    print("The following messages are available:")
                    for i in range(len(messages)):
                        print("    " + str(i+1) + ". (length = " + str(len(messages[i])) + ")")
                    message_number = int(input("Enter your choice: "))
                    print("Decrypted message: ", messages[message_number-1])
                elif user_choice == "2":
                    message = input("Enter a message to sign: ")
                    signature = rsa_instance.encrypt(message, rsa_instance.private_key)
                    rsa_instance.newFile(signature, "signatures")
                    print("Message signed and sent")
                elif user_choice == "3":
                    print("Public Key:", rsa_instance.public_key)
                    print("Private Key:", rsa_instance.private_key)
                elif user_choice == "4":
                    rsa_instance = RSA(1024)  # Generate a new set of keys
                    print("New set of keys generated.")
                elif user_choice == "5":
                    break
                else:
                    print("Invalid input. Please try again.")

        elif user_type == "3":
            print("Bye for now!")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()