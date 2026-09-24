import alchemy
import elements
from alchemy import strength_potion


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to gold: brew '{alchemy.create_air()}' "
            f"and '{strength_potion()}' mixed with '{elements.create_fire()}'")
