def main():
    """Simulates crisis response system for archive access attempts."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        file = "lost_archive.txt"
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        with open(file, "r") as f:
            print("SUCCESS: Archive recovered - '", f.read(), "'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, system stable\n")

    try:
        file = "classified_vault.txt"
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        with open(file, "r") as f:
            print("SUCCESS: Archive recovered - '", f.read(), "'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained\n")

    try:
        file = "standard_archive.txt"
        print(f"ROUTINE ALERT: Attempting access to '{file}'...")
        with open(file, "r") as f:
            print("SUCCESS: Archive recovered - '", f.read(), "'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
