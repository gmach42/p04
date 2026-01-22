#!/usr/bin/env python3
import sys


def collect_input() -> tuple[str, str]:
    """Collects archivist ID and status report from input stream."""
    print("Input Stream active. ", end="")
    arch_id = input("Enter archivist ID: ")
    print("Input Stream active. ", end="")
    status_report = input("Enter status report: ")
    print("")
    return arch_id, status_report


def standard_message(message: str) -> None:
    """Sends a standard message to stdout."""
    sys.stdout.write(f"[STANDARD] {message}\n")


def alert_message(message: str) -> None:
    """Sends an alert message to stderr."""
    sys.stderr.write(f"[ALERT] {message}\n")


def main():
    """Simulates a communication system for cyber archives."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        arch_id, status_report = collect_input()
        standard_message(f"Archive status from {arch_id}: {status_report}")
        alert_message("System diagnostic: Communication channels verified")
        standard_message("Data transmission complete")
    except Exception as e:
        print(f"\nError during communication: {e}\n")
    else:
        print("\nThree channel communication test successful.")


if __name__ == "__main__":
    main()
