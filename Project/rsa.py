import ast
import os
import random


class RSA:
    def __init__(self, key_length=1024):
        # Check for existing keys and load them if they exist
        if not self.load_keys():
            self.public_key, self.private_key = self.rsa_keygen(key_length)
            self.public_sign_key, self.private_sign_key = self.rsa_keygen(key_length)
            # Save the newly generated keys
            self.save_keys()

    def load_keys(self):
        keys_path = "keys"
        try:
            if os.path.exists(os.path.join(keys_path, "public_key.pem")) and os.path.exists(os.path.join(keys_path, "private_key.pem")) and os.path.exists(os.path.join(keys_path, "public_sign_key.pem")) and os.path.exists(os.path.join(keys_path, "private_sign_key.pem")):
                with open(os.path.join(keys_path, "public_key.pem"), "r") as file:
                    self.public_key = ast.literal_eval(file.read())
                with open(os.path.join(keys_path, "private_key.pem"), "r") as file:
                    self.private_key = ast.literal_eval(file.read())
                with open(os.path.join(keys_path, "public_sign_key.pem"), "r") as file:
                    self.public_sign_key = ast.literal_eval(file.read())
                with open(os.path.join(keys_path, "private_sign_key.pem"), "r") as file:
                    self.private_sign_key = ast.literal_eval(file.read())
                return True
        except Exception as e:
            print(f"Error loading keys: {e}")
        return False

    def save_keys(self):
        keys_path = "keys"
        if not os.path.exists(keys_path):
            os.makedirs(keys_path)
        with open(os.path.join(keys_path, "public_key.pem"), "w") as file:
            file.write(str(self.public_key))
        with open(os.path.join(keys_path, "private_key.pem"), "w") as file:
            file.write(str(self.private_key))
        with open(os.path.join(keys_path, "public_sign_key.pem"), "w") as file:
            file.write(str(self.public_sign_key))
        with open(os.path.join(keys_path, "private_sign_key.pem"), "w") as file:
            file.write(str(self.private_sign_key))

    def generate_prime_candidate(self, length):
        return random.getrandbits(length)

    def is_prime(self, n, k=128):
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        for _ in range(k):
            a = random.randint(2, n - 2)
            if pow(a, n - 1, n) != 1:
                return False
        return True

    def generate_prime_number(self, length=1024):
        p = 4
        while not self.is_prime(p, 128):
            p = self.generate_prime_candidate(length)
        return p

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def multiplicative_inverse(self, e, phi):
        m0, x0, x1 = phi, 0, 1
        while e > 1:
            q = e // phi
            t = phi
            phi, e = e % phi, t
            t = x0
            x0 = x1 - q * x0
            x1 = t
        return x1 + m0 if x1 < 0 else x1

    def rsa_keygen(self, key_length):
        p = self.generate_prime_number(key_length // 2)
        q = self.generate_prime_number(key_length // 2)
        n = p * q
        phi = (p-1) * (q-1)

        e = 65537
        d = self.multiplicative_inverse(e, phi)

        return ((e, n), (d, n))

    def encrypt(self, plaintext, key=None):
        if key is None:
            key = self.public_key
        key, n = key
        cipher = [pow(ord(char), key, n) for char in plaintext]
        return cipher

    def decrypt(self, ciphertext, key=None):
        if key is None:
            key = self.private_key
        key, n = key
        decrypted_data = bytearray()
        for char in ciphertext:
            decrypted_char = pow(char, key, n)
            decrypted_data.extend(decrypted_char.to_bytes((decrypted_char.bit_length() + 7) // 8, 'big'))
        try:
            return decrypted_data.decode('utf-8')
        except UnicodeDecodeError:
            return decrypted_data.hex()

    def newSignatureFile(self, text, name):
        if not os.path.exists("signatures"):
            os.makedirs("signatures")
        filename = name + ".txt"
        filepath = os.path.join("signatures", filename)
        
        if os.path.exists(filepath):
            print(f"File {filename} already exists. Please try again.")
        else:
            with open(filepath, "w") as file:
                file.write(str(text))

    def getSignatureNames(self):
        dir = "signatures"
        if not os.path.exists(dir):
            print("No signatures available to authenticate.")
            return []
        return [os.path.splitext(filename)[0] for filename in os.listdir(dir)]

    def newFile(self, text, type="messages"):
        if not os.path.exists(type):
            os.makedirs(type)
        filename = ''.join(random.choices('0123456789ABCDEF', k=16)) + ".txt"
        filepath = os.path.join(type, filename)
        
        if os.path.exists(filepath):
            print(f"File {filename} already exists. Please try again.")
        else:
            with open(filepath, "w") as file:
                file.write(str(text))

    def getFiles(self, type="messages", use_decryption=True):
        try: # This line is used to handle exceptions
            dir = type
            if not os.path.exists(dir):
                print(f"No {type} directory found.")
                return []

            files = os.listdir(dir)
            messages = []

            for filename in files:
                filepath = os.path.join(dir, filename)

                try:
                    with open(filepath, "r") as file:
                        content = file.read().strip()
                        encrypted_message = ast.literal_eval(content)

                        if isinstance(encrypted_message, list) and all(isinstance(n, int) for n in encrypted_message):
                            if (use_decryption):
                                decrypted_message = self.decrypt(encrypted_message)
                                messages.append(decrypted_message)
                            else:
                                messages.append(encrypted_message)
                        else:
                            print(f"File {filename} contains invalid encrypted message format.")
                except (SyntaxError, ValueError) as e:
                    print(f"Error reading file {filename}: {e}")

            return messages

        except Exception as e:
            print(f"An unexpected error occurred while retrieving files: {e}")
            return []
    
    def sign(self, message, key=None):
        if key is None:
            key = self.private_sign_key  # Use the private signing key
        key, n = key
        signature = [pow(ord(char), key, n) for char in message]
        return signature

    def verify_signature(self, message, signature, key=None):
        if key is None:
            key = self.public_sign_key  # Use the public signing key for verification
        key, n = key
        decrypted_signature = [pow(char, key, n) for char in signature]
        
        # Convert decrypted signature back to string
        original_message = ''.join([chr(dec_char) for dec_char in decrypted_signature])
        return original_message == message