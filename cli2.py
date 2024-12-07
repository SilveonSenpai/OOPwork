from storage import Storage
from api_client import APIClient
from data_parser import DataParser

def update_character_list():
    """Оновити список персонажів з API та зберегти у сховищі."""
    try:
        print("Updating character list...")
        character_names = APIClient.get_characters()
        if not character_names:
            print("No characters found from the API.")
            return
        
        characters = DataParser.parse_characters(character_names)
        storage = Storage("characters.json")
        storage.save_data([char.to_dict() for char in characters])

        print(f"Successfully updated and saved {len(characters)} characters.")
    except Exception as e:
        print(f"Error updating character list: {e}")


def show_character_details():
    """Показати детальну інформацію про персонажа, включно з графікою."""
    try:
        storage = Storage("characters.json")
        characters = storage.load_data()

        if not characters:
            print("No characters found. Please update the list first.")
            return

        print("Available Characters:")
        for i, char in enumerate(characters, 1):
            print(f"{i}. {char['name']}")

        choice = int(input("Choose a character by number: ")) - 1
        selected_char = characters[choice]

        # Виведення інформації
        print("\nCharacter Details:")
        print(f"Name: {selected_char['name']}")
        print(f"Health: {selected_char.get('health', 'Unknown')}")
        print(f"Armor: {selected_char.get('armor', 'Unknown')}")
        print(f"Attack: {selected_char.get('attack', 'Unknown')}")
        print(f"Description: {selected_char.get('description', 'No description available')}")
        print(f"Image URL: {selected_char.get('image', 'No image available')}")

    except IndexError:
        print("Invalid choice. Please select a valid character number.")
    except Exception as e:
        print(f"Error showing character details: {e}")


def create_new_character():
    """Створити нового персонажа через діалог та зберегти у сховищі."""
    try:
        storage = Storage("characters.json")
        characters = storage.load_data() or []

        print("Enter details for the new character:")
        name = input("Name: ")
        health = int(input("Health: "))
        armor = int(input("Armor: "))
        attack = int(input("Attack: "))
        description = input("Description: ")
        image = input("Image URL (optional): ")

        new_character = {
            "name": name,
            "health": health,
            "armor": armor,
            "attack": attack,
            "description": description,
            "image": image or "No image available"
        }

        characters.append(new_character)
        storage.save_data(characters)

        print(f"New character '{name}' created and saved successfully!")

    except ValueError:
        print("Invalid input. Please enter the correct values.")
    except Exception as e:
        print(f"Error creating new character: {e}")
