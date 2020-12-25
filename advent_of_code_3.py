def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "wurde nicht gefunden.")
        quit()

    data = file.readlines()
    file.close()
    return data

def tree_traverse(data):
    # something mod 31 in this case
    position = 0
    tree_count = 0
    interupt = 0
    for line in data:
        print(line[position])
        width = len(line) - 1
        position += 3
        position = position % width
        interupt += 1
        if line[position] == "#":
            tree_count += 1
            print(tree_count)
            # print(f"---|{line[position]}|---")
        if interupt == 12:
            break    

def main():
    data = read_data("advent_of_code_3.txt")
    tree_traverse(data)

if __name__ == "__main__":
    main()