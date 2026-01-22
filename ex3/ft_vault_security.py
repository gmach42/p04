#!/usr/bin/env python3

def main():
    """Simulates secure vault access and data extraction process."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        classified_file = "classified_data.txt"

        with open(classified_file, "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file.read(), "")

        with open(classified_file, "a") as file:
            print("SECURE PRESERVATION:")
            file.write("[CLASSIFIED] New security protocols archived.\n")
            print("[CLASSIFIED] New security protocols archived.")
        print("Vault automatically sealed after operations.\n")

    except FileNotFoundError:
        print("ERROR: Classified storage vault not found.")
    except PermissionError:
        print("ERROR: You do not have permission to access the vault.")
    except AttributeError:
        print("ERROR: Invalid file operation attempted.")

    else:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
