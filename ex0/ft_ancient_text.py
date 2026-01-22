#!/usr/bin/env python3

def main():
    """Simulates data recovery from an ancient text file."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file_name: str = "ancient_fragment.txt"
    try:
        print(f"\nAccessing Storage Vault: {file_name}")
        file = open(file_name, 'r')
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.\n")
    else:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
