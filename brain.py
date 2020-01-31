import random
def brain(array_length):
    instructions = []
    for n in range(array_length):
        movement = (random.randint(-5,5),random.randint(-5,5))
        instructions.append(movement)
    return instructions

