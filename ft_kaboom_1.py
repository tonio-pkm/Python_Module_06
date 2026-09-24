if __name__ == "__main__":
    ingredients = "Earth, wind and fire"
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimore/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN EXCEPTION")
    try:
        from alchemy.grimore.dark_spellbook import dark_spell_record
        print(f"Testing record dark spell: "
              f"{dark_spell_record('Fantasy', ingredients)}")
    except Exception as e:
        print(f"Caught exception: {e}")
