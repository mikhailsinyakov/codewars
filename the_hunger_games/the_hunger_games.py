predators = {
    "antelope": ["grass"],
    "big-fish": ["little-fish"],
    "bug": ["leaves"],
    "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
    "chicken": ["bug"],
    "cow": ["grass"],
    "fox": ["chicken", "sheep"],
    "giraffe": ["leaves"],
    "lion": ["antelope", "cow"],
    "panda": ["leaves"],
    "sheep": ["grass"]
}


def who_eats_who(zoo):
    animals = zoo.split(",")
    changes = []
    i = 0

    while i < len(animals):
        predator = animals[i]
        prey1 = animals[i-1] if i > 0 else None
        prey2 = animals[i+1] if i < len(animals) - 1 else None

        if prey1 in predators.get(predator, []):
            changes.append((predator, prey1))
            animals.pop(i-1)
            i = max(i-2, 0)
            continue

        if prey2 in predators.get(predator, []):
            changes.append((predator, prey2))
            animals.pop(i+1)
            continue

        i += 1

    return [zoo] + [f"{predator} eats {prey}" for predator, prey in changes] + [",".join(animals)]
