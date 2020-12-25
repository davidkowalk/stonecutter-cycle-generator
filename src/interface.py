from sys import argv as args
import generator

def help():
    print("""
Format: python interface.py <Destination Folder> [<id1> <id2> <id2>...]
    """)

def main():

    if len(args) == 1:
        help()
        exit()

    folder = args[1]
    ids = args[2:]

    recipes, pairs = generator.gen_contents(ids)

    for id in range(len(pairs)):
        pair = pairs[id]
        filename = pair[0] + "_" + pair[1] + ".json"

        recipe = recipes[id]

        with open(folder+"/"+filename, "w") as f:
            f.write(recipe)

if __name__ == '__main__':
    main()
