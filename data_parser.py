from characters import BasicCharacter
from items import Weapon, BasicWeapon
from api_client import APIClient
class DataParser:
    @staticmethod
    def parse_character(data):
        """
        Парсинг даних персонажа у формат BasicCharacter.
        """
        try:
            return BasicCharacter(
                name=data["name"],
                health=data.get("health", 100),  
                armor=data.get("armor", 20),
                attack=data.get("attack", 30),
                description=data.get("description", "No description available"),
                vision=data.get("vision", "Unknown"),
                weapon=data.get("weapon", "Unknown"),
                rarity=data.get("rarity", 1),
                birthday=data.get("birthday", "Unknown"),
                nation=data.get("nation", "Unknown"),
                constellation=data.get("constellation", "Unknown"),
                talents=data.get("skillTalents", [])
            )
        except KeyError as e:
            print(f"Missing key in character data: {e}")
            return None

    @staticmethod
    def parse_characters(data_list):
        """
        Парсинг списку персонажів із API.
        Якщо список містить лише імена, виконується додатковий запит до API.
        """
        if not isinstance(data_list, list):
            raise TypeError(f"Expected a list, but got {type(data_list)}")

        characters = []
        for item in data_list:
            if isinstance(item, str):  
                character_data = APIClient.get_character_details(item)
                characters.append(DataParser.parse_character(character_data))
            elif isinstance(item, dict):  
                characters.append(DataParser.parse_character(item))
            else:
                print(f"Unexpected item type in character list: {type(item)}")
        return characters
    @staticmethod
    def parse_weapon(data):
        """
        Парсинг даних зброї у формат BasicWeapon.
        """
        try:
            return BasicWeapon(
                name=data["name"],
                attack_bonus=data.get("attack", 10),  
                rarity=data.get("rarity", 1),
                description=data.get("description", "No description available"),
            )
        except KeyError as e:
            print(f"Missing key in weapon data: {e}")
            return None

    @staticmethod
    def parse_weapons(data_list):
        """
        Парсинг списку зброї із API.
        """
        if not isinstance(data_list, list):
            raise TypeError(f"Expected a list, but got {type(data_list)}")

        weapons = []
        for item in data_list:
            if isinstance(item, str): 
                weapon_data = APIClient.get_weapon_details(item)
                weapons.append(DataParser.parse_weapon(weapon_data))
            elif isinstance(item, dict):  
                weapons.append(DataParser.parse_weapon(item))
            else:
                print(f"Unexpected item type in weapon list: {type(item)}")
        return weapons




