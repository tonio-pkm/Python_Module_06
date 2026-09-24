from alchemy.grimore import light_spell_record

if __name__ == "__main__":
    ingredients = "Earth, wind and fire"
    print("=== Kaboom 0 ===")
    print("Using grimore module directly")
    print(f"Testing record light spell: "
          f"{light_spell_record('Fantasy', ingredients)}")
