#!/usr/bin/env python3
import sys


def collect_input():
    print("Input Stream active. ", end="")
    arch_id = input("Enter archivist ID: ")
    print("Input Stream active. ", end="")
    status_report = input("Enter status report: ")
    print("\n")
    return arch_id, status_report


def standard_message(message: str):
    sys.stdout.write(f"[STANDARD] {message}\n")


def alert_message(message: str):
    sys.stderr.write(f"[ALERT] {message}\n")


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arch_id, status_report = collect_input()
    try:
        standard_message(f"Archive status from {arch_id}: {status_report}")
        alert_message(f"Archive status from {arch_id}: {status_report}")
        standard_message("Data transmission complete")
    except Exception as e:
        print(f"Error during communication: {e}")
        return
    print("\nThree channel communication test successful.")


if __name__ == "__main__":
    main()
