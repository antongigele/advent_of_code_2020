def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "wurde nicht gefunden.")
        quit()

    data = file.readlines()
    file.close()
    return data

def tree_traverse(data, right):
    position = 0 # startposition
    tree_count = 0
    for line in data:
        width = len(line) - 1 # breite von den zeilen
        letter = line[position]
        if "#" in letter:
            tree_count += 1

        position += right
        position = position % width  # verschiebe position um mod breite
    print(tree_count)
def main():
    data = read_data("advent_of_code_3.txt")
    tree_traverse(data,3)

if __name__ == "__main__":
    main()