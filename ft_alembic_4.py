import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accesing the alchemy module using 'import alchemy'")
    try:
        print(f"Testing create_air: {alchemy.create_air()}")
    except AttributeError:
        print("import error")
    print("Now show that not all functions can be reached\n"
          "This will raise an exception!")
    try:
        print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
    except AttributeError as e:
        print(f"Testing the hidden create_earth: {e}")
