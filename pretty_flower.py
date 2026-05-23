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
