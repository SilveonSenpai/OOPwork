import unittest
from api_client import APIClient
from data_parser import DataParser
from storage import Storage

class TestInfra(unittest.TestCase):
    def test_api_client(self):
        """
        Перевірка отримання персонажів із API.
        """
        try:
            characters = APIClient.get_characters()
            self.assertIsInstance(characters, list)
            self.assertGreater(len(characters), 0)
        except Exception as e:
            self.fail(f"API Client failed: {e}")

    def test_data_parser(self):
        """
        Перевірка парсингу даних персонажів.
        """
        names = ["Diluc", "Barbara", "Kaeya"]
        characters = DataParser.parse_characters(names)
        self.assertEqual(len(characters), len(names))
        self.assertTrue(all(char.name in names for char in characters))

    def test_storage(self):
        """
        Перевірка функцій збереження та завантаження.
        """
        storage = Storage("test_data.json")
        test_data = {"characters": ["Diluc", "Barbara"]}
        storage.save(test_data)

        loaded_data = storage.load()
        self.assertEqual(test_data, loaded_data)

if __name__ == "__main__":
    unittest.main()

