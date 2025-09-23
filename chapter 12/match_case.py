def example(status):
    match status:
        case "hp":
            return "you have 100 health points"
        case "atk":
            return "you did 30 damage"
        case "mp":
            return "you have 80 magic points"
        case _:
            return "404, not found."
        
print(example("hp"))
print(example("baabab"))
print(example("atk"))
print(example("mp"))
