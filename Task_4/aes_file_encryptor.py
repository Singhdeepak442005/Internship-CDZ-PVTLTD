import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"


def generate_key():
    """
    Generate and save encryption key.
    """
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

    print("[+] Encryption Key Generated Successfully.")


def load_key():

    if not os.path.exists(KEY_FILE):
        generate_key()

    return open(KEY_FILE, "rb").read()


def encrypt_file(filename):

    key = load_key()

    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    encrypted_file = filename + ".encrypted"

    with open(encrypted_file, "wb") as file:
        file.write(encrypted_data)

    print(f"\n[✓] File Encrypted Successfully")
    print(f"Encrypted File : {encrypted_file}")


def decrypt_file(filename):

    key = load_key()

    cipher = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    output_file = filename.replace(".encrypted", "")

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print(f"\n[✓] File Decrypted Successfully")
    print(f"Decrypted File : {output_file}")


def main():

    print("=" * 50)
    print("        AES-256 FILE ENCRYPTOR")
    print("=" * 50)

    print("\n1. Encrypt File")
    print("2. Decrypt File")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        filename = input("Enter File Name : ")

        if os.path.exists(filename):
            encrypt_file(filename)
        else:
            print("File Not Found!")

    elif choice == "2":

        filename = input("Enter Encrypted File Name : ")

        if os.path.exists(filename):
            decrypt_file(filename)
        else:
            print("File Not Found!")

    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()