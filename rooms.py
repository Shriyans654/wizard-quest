import random

types = [
    "cavern",
    "gatehouse",
    "storeroom",
    "greathall",
    "kitchen",
    "solarium",
    "chapel",
    "crypt",
    "catacomb",
    "armory",
]

adjectives = [
    "dark",
    "brightly lit",
    "dank",
    "dry",
    "humid",
    "spooky",
    "massive",
    "huge",
    "spacious",
    "eerie",
]

adjectives_2 = ["sparkling", "mysterious", "whimsical", "enchanting", "radiant"]

features = [
    "ancient treasure chest",
    "crumbling statue",
    "hidden passage",
    "magical portal",
    "forgotten inscription",
]


def create_room():
    room_type = random.choice(types)
    adj_1 = random.choice(adjectives)
    adj_2 = random.choice(adjectives_2)
    feature = random.choice(features)

    description = f"""You find yourself in a {adj_1} {adj_2} {room_type} with a {feature}."""

    return description    
