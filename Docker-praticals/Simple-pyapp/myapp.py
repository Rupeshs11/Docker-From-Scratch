FILENAME = "users.txt"

def add_user(name):
    with open(FILENAME, "a") as f:
        f.write(name + "\n")

def show_users():
    try:
        with open(FILENAME, "r") as f:
            users = f.readlines()
            if not users:
                print("No users found.")
            else:
                print("\nStored Users:")
                for user in users:
                    print("-", user.strip())
    except FileNotFoundError:
        print("No users file found.")

def main():
    name = input("Enter your name: ")
    add_user(name)

    choice = input("Do you want to see all users? (y/n): ").lower()
    if choice == "y":
        show_users()
    else:
        print("Okay, not showing users.")

if __name__ == "__main__":
    main()
