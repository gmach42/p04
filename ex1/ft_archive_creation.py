#!/user/bin/env python3


def create_archive(name: str) -> object:
    """function to create a new archive file"""
    print(f"\nInitializing new storage unit: {name}")
    file = open(name, "w")
    print("Storage unit created successfully...")
    return file


def write_archive(file: object) -> None:
    """function to write in the archive precious data"""
    print("\nInscribing preservation data..")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347%")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("[ENTRY 003] Archived by Data Archivist trainee")
    print("Data inscription complete!\n")


def close_archive(file: object) -> None:
    """function to close the archive"""
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive {file.name} ready for long-term preservation.\n")


def main():
    """Simulates archive creation and data inscription process."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    file = create_archive("new_discovery.txt")
    try:
        write_archive(file)
        close_archive(file)
    except AttributeError:
        print("Error: Invalid file object")


if __name__ == "__main__":
    main()
