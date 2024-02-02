




def sign_message(message, private_key):
    checksum = sum(ord(char) for char in message) % 101
    signature = (checksum ** private_key) % 101
    return signature
def verify_signature(message, signature, public_key):
    checksum = sum(ord(char) for char in message) % 101
    expected_checksum = (signature ** 2) % 101
    return checksum == expected_checksum




