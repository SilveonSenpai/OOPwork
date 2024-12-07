import requests
import time

class APIClient:
    BASE_URL = "https://genshin.jmp.blue"

    @staticmethod
    def get_characters(retries=3, delay=2):
        """
        Отримати список імен персонажів із зовнішнього API.
        """
        url = f"{APIClient.BASE_URL}/characters"
        for attempt in range(retries):
            try:
                response = requests.get(url)
                print(f"Response status code: {response.status_code}")  
                print(f"Response text: {response.text}") 
                if response.status_code == 200:
                    return response.json()
                print(f"API Error: {response.status_code}. Retrying in {delay} seconds...")
            except requests.RequestException as e:
                print(f"Request failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
        raise Exception("API is unavailable after multiple attempts.")

    @staticmethod
    def get_character_details(character_name, retries=3, delay=2):
        """
        Отримати детальну інформацію про персонажа за його іменем.
        """
        url = f"{APIClient.BASE_URL}/characters/{character_name}"
        for attempt in range(retries):
            try:
                response = requests.get(url)
                print(f"Response for {character_name}: {response.text}")  
                if response.status_code == 200:
                    try:
                        return response.json()  
                    except ValueError:
                        print(f"Error: Response for {character_name} is not valid JSON.")
                        return {"error": "Invalid JSON response"}
                print(f"API Error for {character_name}: {response.status_code}. Retrying in {delay} seconds...")
            except requests.RequestException as e:
                print(f"Request for {character_name} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
        raise Exception(f"API is unavailable for character {character_name} after multiple attempts.")



    @staticmethod
    def get_weapons(retries=3, delay=2):
        """Отримати список імен зброї із зовнішнього API."""
        url = f"{APIClient.BASE_URL}/weapons"
        for attempt in range(retries):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    return response.json()
                print(f"API Error: {response.status_code}. Retrying in {delay} seconds...")
            except requests.RequestException as e:
                print(f"Request failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
        raise Exception("API is unavailable after multiple attempts.")

    @staticmethod
    def get_weapon_details(weapon_name, retries=3, delay=2):
        """Отримати детальну інформацію про зброю за її ім'ям."""
        url = f"{APIClient.BASE_URL}/weapons/{weapon_name}"
        for attempt in range(retries):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    return response.json()
                print(f"API Error for {weapon_name}: {response.status_code}. Retrying in {delay} seconds...")
            except requests.RequestException as e:
                print(f"Request for {weapon_name} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
        raise Exception(f"API is unavailable for weapon {weapon_name} after multiple attempts.")
