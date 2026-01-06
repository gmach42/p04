

def handle_crisis(file):
    try:
        with open(file, "r") as f:
            data = f.read()
            if "CLASSIFIED" in data:
                raise PermissionError("Security protocols deny access")
            return data

    except FileNotFoundError:
        raise FileNotFoundError("Archive not found in storage matrix")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files_to_open = [
        "lost_archive.txt", "classified_data.txt", "standard_archive.txt"]
    for file in files_to_open:
        try:
            content = handle_crisis(file)
            print(f"ROUTINE ACCESS: Attempting access to {file}")
            print(f"SUCCESS: Archive recovered - {content}")
            print("STATUS: Normal operations resumed\n")

        except Exception as e:
            print(f"CRISIS ALERT: Attempting access to {file}")
            print(f"RESPONSE: {e}")
            if isinstance(e, FileNotFoundError):
                print("STATUS: Crisis handled, system stable\n")
            elif isinstance(e, PermissionError):
                print("STATUS: Crisis handled, security maintained\n")
            else:
                print(
                    "STATUS: Unknown error, further investigation required\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
