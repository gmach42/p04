#!/user/bin/env python3


def create_archive(name: str):
    """function to create a new archive file"""
    print(f"\nInitializing new storage unit: {name}")
    try:
        file = open(name, "x")
        print("Storage unit created successfully...")
        return file
    except FileExistsError as e:
        print(f"Error: {e}")
        return None


def write_archive(file):
    """function to write in the archive precious data"""
    print("\nInscribing preservation data..")
    try:
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        print("[ENTRY 001] New quantum algorithm discovered")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        print("[ENTRY 002] Efficiency increased by 347%")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("[ENTRY 003] Archived by Data Archivist trainee")
    except AttributeError as e:
        return f"Error: {e}"


def close_archive(file):
    """function to close the archive"""
    try:
        file.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive {file.name} ready for long-term preservation.")
    except AttributeError as e:
        print(f"Error: {e}")


def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    file = create_archive("new_discovery.txt")
    if file is not None:
        write_archive(file)
        close_archive(file)


if __name__ == "__main__":
    main()
