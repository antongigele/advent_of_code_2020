def readData(path):
    try:
        file = open(path, "r")
    except:
        print("Das File ", path, "wurde nicht gefunden.")
        quit()    

    data = file.readlines()
    file.close()

    return data
def checkpassword_part1(data):
    number_valid_passwords = 0
    for line in data:
        line_list = line.split()
        if line_list[1][0] not in line_list[2]:
            pass
            # print("password doesn't fullfill the requirements.")
        else:
            count = 0
            for letter in line_list[2]:
                if letter == line_list[1][0]:
                    count += 1
                else:
                    pass
            first_entry_list = line_list[0].split('-')
            # print(f"{first_entry_list[0]} - {first_entry_list[1]}")   
            if count >= int(first_entry_list[0]) and count <= int(first_entry_list[1]):
                number_valid_passwords += 1
                # print("password fullfills requirements.")
            else:
                pass
                # print("password doesn't fullfill the requirements.")
                # print(f"{first_entry_list[0]} -{count}- {first_entry_list[1]}")       
    print(f"The number of valid passwords is: {number_valid_passwords}")

def checkpassword_part2(data):
    number_valid_passwords = 0
    for line in data:
        line_list = line.split()
        letter = line_list[1][0]
        if letter not in line_list[2]:
            pass
            # print("password doesn't fullfill the requirements.")
        else:
            first_entry_list = line_list[0].split('-')

            first_position = line_list[2][int(first_entry_list[0])-1]
            second_position = line_list[2][int(first_entry_list[1])-1]

            if len(line_list[2]) < int(first_entry_list[1]):
                pass
            else:
                if ((letter == first_position and not letter == second_position) or
                    (letter == second_position and not letter == first_position)):
                    number_valid_passwords += 1
                    # print("password fullfills requirements.")
                else:
                    pass
                    # print("password doesn't fullfill the requirements.")

    print(f"The number of valid passwords is: {number_valid_passwords}")


def main():
    data = readData("advent_of_code_2.txt")
    checkpassword_part1(data)
    checkpassword_part2(data)

if __name__ == "__main__":
    main()   