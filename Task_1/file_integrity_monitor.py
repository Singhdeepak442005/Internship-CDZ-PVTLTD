import hashlib
import json
import os

HASH_FILE = "hashes.json"

# Function to calculate SHA-256 hash
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


# Load saved hashes
def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as file:
            return json.load(file)
    return {}


# Save hashes
def save_hashes(hashes):
    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)


def main():
    hashes = load_hashes()

    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("❌ File not found!")
        return

    current_hash = calculate_hash(file_path)

    if file_path in hashes:
        if hashes[file_path] == current_hash:
            print("\n✅ File Integrity Verified.")
            print("No changes detected.")
        else:
            print("\n⚠ WARNING!")
            print("File has been modified!")
            print("Old Hash :", hashes[file_path])
            print("New Hash :", current_hash)
    else:
        print("\n📁 New file detected.")
        print("Hash stored successfully.")

    hashes[file_path] = current_hash
    save_hashes(hashes)


if __name__ == "__main__":
    main()