def insert_stems(lines, index, count):
    if count == 0:
        return 

    lines.insert(index, "          ||\n")
    return insert_stems(lines, index + 1, count - 1)

def modify_flower():
    try:
        stem_length = int(input("How long do you want your stems? "))
    except ValueError:
        print("Please put in a valid integer.")
        return
    with open("pretty_flower.txt", "r") as file:
        lines = file.readlines()
    
    starting_stem = 8
    new_lines = insert_stems(lines, starting_stem, stem_length)
    with open("pretty_long_flower.txt", "w") as file: 
        file.writelines(lines)

    
    