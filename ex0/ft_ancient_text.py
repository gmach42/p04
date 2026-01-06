#!/usr/bin/env python3


def access_vault(file):
    """function to open a file"""
    print(f"Accessing Storage Vault: {file}")
    try:
        f = open(file, "r")
        print("Connection established...\n")
        return (f)
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
        return None


def read_vault(file):
    """function to read a file"""
    print("RECOVERED DATA:")
    try:
        print(file.read())
        print("\n")
    except AttributeError as e:
        print(f"Error: {e}")


def close_vault(file):
    """function to close a file"""
    try:
        file.close()
        print("Data recovery complete. Storage unit disconnected.\n")
    except AttributeError as e:
        print(f"Error: {e}")


def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = access_vault("ancient_fragment.txt")
    if file is not None:
        read_vault(file)
        close_vault(file)


if __name__ == "__main__":
    main()
