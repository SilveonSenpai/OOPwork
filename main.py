from cli2 import update_character_list, show_character_details, create_new_character

def run_cli():
    """Головний цикл CLI для взаємодії з користувачем."""
    while True:
        print("\nGame System CLI")
        print("1. Update Character List")
        print("2. Show Character Details")
        print("3. Create New Character")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            update_character_list()
        elif choice == "2":
            show_character_details()
        elif choice == "3":
            create_new_character()
        elif choice == "4":
            print("Exiting CLI. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    run_cli()
