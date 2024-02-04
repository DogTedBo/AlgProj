from rsa import RSA

class RSAManager:
    def __init__(self):
        self.rsa_instance = RSA(1024)

    def public_user_menu(self):
        while True:
            print("\nAs a public user, what would you like to do?")
            print("1. Send an encrypted message")
            print("2. Authenticate a digital signature")
            print("3. Exit")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                self.send_encrypted_message()
            elif user_choice == "2":
                self.authenticate_signature()
            elif user_choice == "3":
                break
            else:
                print("Invalid input. Please try again.")

    def send_encrypted_message(self):
        message = input("Enter a message: ")
        encrypted_msg = self.rsa_instance.encrypt(message)
        self.rsa_instance.newFile(encrypted_msg)
        print("Message encrypted and sent")

    def authenticate_signature(self):
        signatures = self.rsa_instance.getFiles("signatures")
        if not signatures:
            print("No signatures available to authenticate.")
            return

        print("The following messages are available:")
        for i, signature in enumerate(signatures, 1):
            print(f"{i}. {signature}")

        message_number = int(input("Enter your choice: "))
        print("Signature authenticated")

    def owner_menu(self):
        while True:
            print("\nAs the owner of the keys, what would you like to do?")
            print("1. Decrypt a received message")
            print("2. Digitally sign a message")
            print("3. Show the keys")
            print("4. Generate a new set of keys")
            print("5. Exit")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                self.decrypt_received_message()
            elif user_choice == "2":
                self.sign_message()
            elif user_choice == "3":
                self.show_keys()
            elif user_choice == "4":
                self.generate_new_keys()
            elif user_choice == "5":
                break
            else:
                print("Invalid input. Please try again.")

    def decrypt_received_message(self):
        messages = self.rsa_instance.getFiles()
        if not messages:
            print("No messages available to decrypt.")
            return

        print("The following messages are available:")
        for i, msg in enumerate(messages, 1):
            print(f"    {i}. (length = {len(msg)})")

        message_number = int(input("Enter your choice: "))
        print("Decrypted message:", messages[message_number - 1])

    def sign_message(self):
        message = input("Enter a message to sign: ")
        signature = self.rsa_instance.encrypt(message, self.rsa_instance.private_key)
        self.rsa_instance.newFile(signature, "signatures")
        print("Message signed and sent")

    def show_keys(self):
        print("Public Key:", self.rsa_instance.public_key)
        print("Private Key:", self.rsa_instance.private_key)

    def generate_new_keys(self):
        self.rsa_instance = RSA(1024)
        print("New set of keys generated.")

def main():
    rsa_manager = RSAManager()

    while True:
        print("\nPlease select your user type:")
        print("1. A public user")
        print("2. The owner of the keys")
        print("3. Exit program")
        user_type = input("Enter your choice: ")

        if user_type == "1":
            rsa_manager.public_user_menu()
        elif user_type == "2":
            rsa_manager.owner_menu()
        elif user_type == "3":
            print("Bye for now!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
