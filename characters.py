from abc import ABC, abstractmethod
from damage import DamageType

class Character(ABC):
    """Abstract base class for game characters."""
    
    def __init__(self, name, health, armor, attack):
        self._name = name
        self._health = health
        self._armor = armor
        self._attack = attack
        self._status_effects = {}
        self._equipped_items = []

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def armor(self):
        return self._armor

    @property
    def attack(self):
        return self._attack

    def to_dict(self):
        """Serialize character to dictionary."""
        return {
            "name": self._name,
            "health": self._health,
            "armor": self._armor,
            "attack": self._attack,
            "status_effects": self._status_effects,
            "equipped_items": [item.name for item in self._equipped_items],
        }

    @classmethod
    def from_dict(cls, data):
        """Deserialize character from dictionary."""
        character = cls(
            name=data["name"],
            health=data["health"],
            armor=data["armor"],
            attack=data["attack"],
        )
        return character

    def equip_item(self, item):
        """Equip an item and apply its effects."""
        item.apply(self)
        self._equipped_items.append(item)
    
    def unequip_item(self, item):
        """Unequip an item and remove its effects."""
        if item in self._equipped_items:
            item.remove(self)
            self._equipped_items.remove(item)

    def take_damage(self, amount, damage_type: DamageType):
        """Reduce health based on incoming damage and damage type."""
        damage = damage_type.calculate_damage(amount, self)
        self._health = max(0, self._health - damage)  # Prevent negative health
        print(f"{self._name} takes {damage} {damage_type.name} damage!")
        damage_type.apply_effects(self)  # Apply status effects if any

    def apply_status_effect(self, effect_name, duration, damage_per_turn):
        """Apply a status effect with duration and periodic damage."""
        self._status_effects[effect_name] = {"duration": duration, "damage_per_turn": damage_per_turn}
    
    def process_status_effects(self):
        """Handle status effect processing at the start of each turn."""
        for effect, data in list(self._status_effects.items()):
            print(f"{self._name} suffers {data['damage_per_turn']} damage from {effect}!")
            self._health = max(0, self._health - data['damage_per_turn'])
            data["duration"] -= 1
            if data["duration"] <= 0:
                print(f"{self._name} is no longer affected by {effect}.")
                del self._status_effects[effect]

    def increase_attack(self, value):
        self._attack += value

    def decrease_attack(self, value):
        self._attack -= value

    def increase_armor(self, value):
        self._armor += value

    def decrease_armor(self, value):
        self._armor -= value

    @abstractmethod
    def use_ability(self, target):
        """Abstract method for character abilities."""
        pass

    def is_alive(self):
        """Check if the character is still alive."""
        return self._health > 0

class BasicCharacter(Character):
    """Concrete implementation of a basic character."""

    def __init__(self, name, health, armor, attack, description="", vision="", weapon="",
                 rarity=1, birthday="Unknown", nation="Unknown", constellation="Unknown", talents=None):
        super().__init__(name, health, armor, attack)
        self.description = description
        self.vision = vision
        self.weapon = weapon
        self.rarity = rarity
        self.birthday = birthday
        self.nation = nation
        self.constellation = constellation
        self.talents = talents or []

    def use_ability(self, target):
        print(f"{self.name} uses a basic attack on {target.name}!")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "description": self.description,
            "vision": self.vision,
            "weapon": self.weapon,
            "rarity": self.rarity,
            "birthday": self.birthday,
            "nation": self.nation,
            "constellation": self.constellation,
            "talents": self.talents
        })
        return data
class Memento:
    """Клас для збереження стану персонажа."""
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    """Клас для управління збереженнями."""
    def __init__(self):
        self._mementos = []

    def save(self, memento):
        self._mementos.append(memento)

    def undo(self):
        if not self._mementos:
            print("No saved states.")
            return None
        return self._mementos.pop()


class State(ABC):
    """Базовий клас для станів персонажа."""
    @abstractmethod
    def handle(self, character):
        pass


class NormalState(State):
    def handle(self, character):
        print(f"{character.name} is in a normal state.")


class BerserkState(State):
    def handle(self, character):
        character.increase_attack(10)
        print(f"{character.name} is in a berserk state! Attack increased.")


class ObservableCharacter(BasicCharacter):
    """Персонаж із можливістю збереження стану та підтримкою станів."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._state = NormalState()
        self._caretaker = Caretaker()

    def set_state(self, state):
        self._state = state

    def handle_state(self):
        self._state.handle(self)

    def save_state(self):
        memento = Memento(self.to_dict())
        self._caretaker.save(memento)
        print(f"State of {self.name} saved.")

    def restore_state(self):
        memento = self._caretaker.undo()
        if not memento:
            print(f"No saved state to restore for {self.name}.")
            return
        state = memento.get_state()
        self._name = state["name"]
        self._health = state["health"]
        self._armor = state["armor"]
        self._attack = state["attack"]
        print(f"State of {self.name} restored.")
        #Observer
    # Додано до ObservableCharacter у characters.py

class Observer(ABC):
    """Базовий клас для спостерігачів."""
    @abstractmethod
    def update(self, subject):
        pass


class HealthObserver(Observer):
    def update(self, subject):
        print(f"HealthObserver: {subject.name}'s health is now {subject.health}.")


class ArmorObserver(Observer):
    def update(self, subject):
        print(f"ArmorObserver: {subject.name}'s armor is now {subject._armor}.")


class ObservableCharacter(ObservableCharacter):  # Спадкування для інтеграції Observer
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def take_damage(self, amount, damage_type: DamageType):
        super().take_damage(amount, damage_type)
        self.notify_observers()

