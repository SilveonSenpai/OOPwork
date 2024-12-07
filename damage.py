from abc import ABC, abstractmethod

class DamageType(ABC):
    """Abstract base class for damage types."""

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def calculate_damage(self, base_damage, character):
        """Calculate actual damage considering the character's armor."""
        pass

    @abstractmethod
    def apply_effects(self, character):
        """Apply additional effects like status conditions."""
        pass


class PhysicalDamage(DamageType):
    """Physical damage, reduced by armor."""

    @property
    def name(self):
        return "Physical"

    def calculate_damage(self, base_damage, character):
        return max(0, base_damage - character._armor)

    def apply_effects(self, character):
        """No additional effects for physical damage."""
        pass


class FireDamage(DamageType):
    """Fire damage, ignores armor and applies burn effect."""

    @property
    def name(self):
        return "Fire"

    def calculate_damage(self, base_damage, character):
        return base_damage  # Fire damage ignores armor

    def apply_effects(self, character):
        """Apply burn effect for 3 turns."""
        character.apply_status_effect("Burn", duration=3, damage_per_turn=5)
