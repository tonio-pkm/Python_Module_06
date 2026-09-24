from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if dark_validate_ingredients(ingredients) == "VALID":
        return (f"Spell recorded: {spell_name} ({ingredients} - VALID)")
    return (f"Spell rejected: {spell_name} ({ingredients} - INVALID)")
