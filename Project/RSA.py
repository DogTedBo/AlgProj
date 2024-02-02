import random
import os
import ast 

"""\
This is the main RSA logic that will be used for our project. It will be used to generate the keys, encrypt and decrypt messages, and save the messages to files.

"""
class RSA:
    def __init__(self, key_length=1024):
        self.public_key, self.private_key = self.rsa_keygen(key_length)

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


    def newFile(self, text, type="messages"):
        if not os.path.exists(type):
            os.makedirs(type)
        filename = ''.join(random.choices('0123456789ABCDEF', k=16)) + ".txt"
        filepath = os.path.join(type, filename)
        with open(filepath, "w") as file:
            file.write(str(text))

    def getFiles(self, type="messages"):
        dir = type
        if not os.path.exists(dir):
            print("No messages directory found.")
            return []
        files = os.listdir(dir)
        messages = []
        for filename in files:
            filepath = os.path.join(dir, filename)
            with open(filepath, "r") as file:
                content = file.read().strip()
                try:
                    # Attempt to safely evaluate the file content
                    encrypted_message = ast.literal_eval(content)
                    if isinstance(encrypted_message, list) and all(isinstance(n, int) for n in encrypted_message):
                        decrypted_message = self.decrypt(encrypted_message)
                        messages.append(decrypted_message)
                    else:
                        print(f"File {filename} contains invalid encrypted message format.")
                except SyntaxError as e:
                    print(f"Syntax error in file {filename}: {e}")
        return messages