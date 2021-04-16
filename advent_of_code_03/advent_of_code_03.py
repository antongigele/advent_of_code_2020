def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "wurde nicht gefunden.")
        quit()

    data = file.readlines()
    file.close()
    return data

def tree_traverse(data, right, down):
    position = 0 # startposition
    tree_count = 0
    
    for k, line in enumerate(data):
        width = len(line) - 1 # breite von den zeilen
        if k % down == 0:
            # print(k % down)
            letter = line[position]
            if "#" in letter:
                tree_count += 1

            position += right
            position = position % width  # verschiebe position um mod breite

    print(tree_count)
    return tree_count
def main():
    data = read_data("advent_of_code_3.txt")
    tree_traverse(data,1,1)
    tree_traverse(data,3,1)
    tree_traverse(data,5,1)
    tree_traverse(data,7,1)
    tree_traverse(data,1,2)
    answer = tree_traverse(data,1,1)*tree_traverse(data,3,1)*tree_traverse(data,5,1)*tree_traverse(data,7,1)*tree_traverse(data,1,2)
    print(answer)

if __name__ == "__main__":
    main()