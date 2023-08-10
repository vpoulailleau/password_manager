import string

CHARACTER_SET_LOWERCASE = string.ascii_lowercase
CHARACTER_SET_UPPERCASE = string.ascii_uppercase
CHARACTER_SET_DIGIT = string.digits
CHARACTER_SET_SPECIAL = "@#$<>()[]+-/*=%"


class Rule:
    def is_valid(self, password: str) -> bool:
        return False


class LengthRule(Rule):
    def __init__(self, min_length: int, max_length: int) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def is_valid(self, password: str) -> bool:
        return self.min_length <= len(password) <= self.max_length


class CharacterSetRule(Rule):
    character_set: str = ""

    def is_valid(self, password: str) -> bool:
        return any(c in password for c in self.character_set)


class ContainsLowercaseRule(CharacterSetRule):
    character_set = CHARACTER_SET_LOWERCASE


class ContainsUppercaseRule(CharacterSetRule):
    character_set = CHARACTER_SET_UPPERCASE


class ContainsDigitRule(CharacterSetRule):
    character_set = CHARACTER_SET_DIGIT


class ContainsSpecialRule(CharacterSetRule):
    character_set = CHARACTER_SET_SPECIAL
