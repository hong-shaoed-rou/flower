def print_pretty_flower():
    file = open("pretty_flower.txt")
    flower = file.read()
    print(flower)
    file.close()

def print_many_flower():
    file = open("many_flowers.txt")
    flower = file.read()
    print(flower)
    file.close()

def recursive_flower(times):
    if (times == 0):
        print()
        print("w _ W _ W _ w")
        print("\\__. w0w .__/")
        return
    else:
        recursive_flower(times -1)
        print("    |. .|     ")    

def flower_death_match(flower_1, flower_2):
    while(flower_1 > 0 and flower_2 > 0):
        flower_1 -= 1
        flower_2 -= 1
        print(f"flower_1 has {flower_1} petals left, flower_2 has {flower_2} petals left")


    if (flower_1 > flower_2):
        print("flower 1 destroyed flower 2!!!")
    elif (flower_1 < flower_2):
        print("flower 2 destroyed flower 1!!!")
    else:
        print("both flowers have no more petals :(, war is painful isn't it...")

    return
