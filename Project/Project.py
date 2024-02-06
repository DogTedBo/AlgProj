from RSA import RSA


class RSAManager:   # This class is used to manage the RSA class
    def __init__(self):
        self.rsa_instance = RSA()
        self.rsa_instance

    def public_user_menu(self): # This function is used to display the menu for the public user
        while True: 
            print("\nAs a public user, what would you like to do?")
            print("1. Send an encrypted message")
            print("2. Authenticate a digital signature")
            print("3. Exit")
            
            try: # This line is used to handle the exception
                user_choice = input("Enter your choice: ")
                if user_choice == "1": # This condition is used to send an encrypted message
                    self.send_encrypted_message() 
                elif user_choice == "2": # This condition is used to authenticate a digital signature
                    self.authenticate_signature()
                elif user_choice == "3":    # This condition is used to exit the program
                    break
                else:
                    print("Invalid input. Please try again.")
            except ValueError:  
                print("Invalid input. Please try again.")
            except Exception as e:
                print(f"Error: {e} occurred. Please try again.")
            except ValueError as ve:
                print(f"Error: {ve} occurred. Please try again.")


    def send_encrypted_message(self): # This function is used to send an encrypted message
        try:
            message = input("Enter a message: ") # This line is used to take the input from the user
            encrypted_msg = self.rsa_instance.encrypt(message) # This line is used to encrypt the message
            self.rsa_instance.newFile(encrypted_msg) # This line is used to save the encrypted message to a file
            print("Message encrypted and sent") # This line is used to print the message
        except Exception as e :
            print(f"Error: {e} occurred while encrypting the message. Please try again.")

    def authenticate_signature(self): # This function is used to authenticate a digital signature
        signatures = self.rsa_instance.getFiles("signatures") # This line is used to get the signatures from the file
        if not signatures: # This condition is used to check if the signatures are available
            print("No signatures available to authenticate.") # This line is used to print the message
            return # This line is used to return the control to the calling function

        print("The following messages are available:") # This line is used to print the message
        for i, signature in enumerate(signatures, 1): # This line is used to iterate through the signatures
            print(f"{i}. {signature}") # This line is used to print the signature

        message_number = int(input("Enter your choice: ")) # This line is used to take the input from the user
        print("Signature authenticated") # This line is used to print the message

    def owner_menu(self): # This function is used to display the menu for the owner of the keys
        while True:
            print("\nAs the owner of the keys, what would you like to do?")
            print("1. Decrypt a received message") 
            print("2. Digitally sign a message")
            print("3. Show the keys")
            print("4. Generate a new set of keys")
            print("5. Exit")

            try: # This line is used to handle the exception
                user_choice = input("Enter your choice: ")
                if user_choice == "1":
                    self.decrypt_received_message() # This line is used to decrypt the received message
                elif user_choice == "2":
                    self.sign_message() # This line is used to sign the message
                elif user_choice == "3":
                    self.show_keys() # This line is used to show the keys    
                elif user_choice == "4":
                    keys = self.generate_new_keys() # This line is used to generate a new set of keys
                    self.rsa_instance.newFile(keys[0], "public_key") # This line is used to save the public key to a file
                    self.rsa_instance.newFile(keys[1], "private_key")
                elif user_choice == "5":
                    break
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
            except Exception as e:
                print(f"Error: {e} occurred. Please try again.")
            except ValueError as ve:
                print(f"Error: {ve} occurred. Please try again.")


    def decrypt_received_message(self): # This function is used to decrypt the received message
        messages = self.rsa_instance.getFiles() # This line is used to get the messages from the file
        if not messages: # This condition is used to check if the messages are available
            print("No messages available to decrypt.") 
            return

        print("The following messages are available:") 
        for i, msg in enumerate(messages, 1): # This line is used to iterate through the messages 
            print(f"    {i}. (length = {len(msg)})") # This line is used to print the message

        message_number = int(input("Enter your choice: ")) # This line is used to take the input from the user
        print("Decrypted message:", messages[message_number - 1]) # This line is used to print the message

    def sign_message(self): # This function is used to sign the message
        message = input("Enter a message to sign: ") # This line is used to take the input from the user
        signature = self.rsa_instance.encrypt(message, self.rsa_instance.private_key) # This line is used to sign the message
        self.rsa_instance.newFile(signature, "signatures") # This line is used to save the signature to a file
        print("Message signed and sent")

    def show_keys(self): # This function is used to show the keys
        print("Public Key:", self.rsa_instance.public_key)
        print("Private Key:", self.rsa_instance.private_key)

    def generate_new_keys(self): # This function is used to generate a new set of keys
        self.rsa_instance = RSA(1024)
        print("New set of keys generated.")
        return self.rsa_instance.public_key, self.rsa_instance.private_key

def main(): # This function is used to call the main function
    rsa_manager = RSAManager() # This line is used to create an instance of the RSAManager class

    while True: # This line is used to run the loop
        print("\nPlease select your user type:")
        print("1. A public user")
        print("2. The owner of the keys")
        print("3. Exit program")
        user_type = input("Enter your choice: ")

        if user_type == "1":
            rsa_manager.public_user_menu() # This line is used to display the menu for the public user
        elif user_type == "2":
            rsa_manager.owner_menu() # This line is used to display the menu for the owner of the keys
        elif user_type == "3":
            print("Bye for now!")   # This line is used to exit the program
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__": 
    main() 
