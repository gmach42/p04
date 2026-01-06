#!/usr/bin/env python3


def safe_vault_access(classified_file: str):
    """function to access the vault with 'with' statement"""
    try:
        print("Initiating secure vault access...")
        with open(classified_file, "r") as file:
            print("Vault connection established with failsafe protocols\n")
        return file
    except FileNotFoundError:
        print("ERROR: Classified storage vault not found.")
        return None


def secure_extraction(file):
    """function to securely extract data from the vault"""
    print("SECURE EXTRACTION:")
    try:
        print(file.read())
        print("\n")
    except AttributeError as e:
        print(f"Error: {e}")


def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file = safe_vault_access("classified_records.txt")
    if file is not None:
        secure_extraction(file)
        secure_preservation(file)
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
