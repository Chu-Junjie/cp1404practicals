"""
Store and display names with their email addresses.

Estimated time: 15 minutes
Actual time: 12 minutes
"""

def main():
    """Prompt for emails and store associated names, then display results."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        default_name = extract_name(email)
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if confirmation == "n":
            name = input("Name: ")
        else:
            name = default_name

        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from the part of the email before '@'."""
    try:
        name_part = email.split('@')[0]
        name_parts = name_part.replace('.', ' ').split()
        return ' '.join(name_parts).title()
    except (IndexError, AttributeError):
        return email  # fallback if format is unexpected


main()