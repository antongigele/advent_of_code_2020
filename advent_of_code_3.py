def read_data(path):
    try:
        file = open(path,r)
    except:
        print("File", path, "wurde nicht gefunden.")
    quit()

    data = file.readlines()
    file.close()
    return data

def tree_traverse(data):
    pass

def main():
    data = read_data()
    tree_traverse(data)

if __name__ == "__main__":
    main()