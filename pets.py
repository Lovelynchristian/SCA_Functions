def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s is {pet_name.title()}")

describe_pet('hamster', 'harry')