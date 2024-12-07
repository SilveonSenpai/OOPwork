class Item:
    """Base class for items."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply(self, character):
        """Apply item's effects to a character."""
        pass

    def remove(self, character):
        """Remove item's effects from a character."""
        pass


class Weapon(Item):
    """Weapon class that increases character attack."""

    def __init__(self, name, attack_boost):
        super().__init__(name, f"Increases attack by {attack_boost}.")
        self.attack_boost = attack_boost

    def apply(self, character):
        character.increase_attack(self.attack_boost)

    def remove(self, character):
        character.decrease_attack(self.attack_boost)

class BasicWeapon:
    """Базовий клас для зброї."""

    def __init__(self, name, attack_bonus=0, rarity=1, description=""):
        self._name = name
        self._attack_bonus = attack_bonus
        self._rarity = rarity
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def attack_bonus(self):
        return self._attack_bonus

    @property
    def rarity(self):
        return self._rarity

    @property
    def description(self):
        return self._description

    def to_dict(self):
        """Серіалізація зброї у словник."""
        return {
            "name": self._name,
            "attack_bonus": self._attack_bonus,
            "rarity": self._rarity,
            "description": self._description,
        }

    @classmethod
    def from_dict(cls, data):
        """Десеріалізація зброї зі словника."""
        return cls(
            name=data["name"],
            attack_bonus=data.get("attack_bonus", 0),
            rarity=data.get("rarity", 1),
            description=data.get("description", ""),
        )

    def apply(self, character):
        """Застосування бонусів зброї до персонажа."""
        character.increase_attack(self._attack_bonus)
        print(f"{character.name} equipped {self._name} (+{self._attack_bonus} attack)")

    def remove(self, character):
        """Скасування бонусів зброї з персонажа."""
        character.decrease_attack(self._attack_bonus)
        print(f"{character.name} unequipped {self._name} (-{self._attack_bonus} attack)")
