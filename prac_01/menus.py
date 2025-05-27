name = input("Enter name: ")

# Show menu
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()

# Loop until user quits
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Show menu again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

print("Finished.")
