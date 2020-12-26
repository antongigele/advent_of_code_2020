def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "wurde nicht gefunden.")
        quit()

    data = file.read()
    file.close()

    return data

def main():
    data = read_data('advent_of_code_5.txt')

if __name__ == "__main__":
    main()     