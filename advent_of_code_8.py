def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "nicht gefunden")
        quit()

    data = file.readlines()
    file.close()
    return data

def listcreater(data, sep = None, replace_old = None, replace_new = None):
    if sep is not None:
        sep_list = data.split(sep)
        if replace_old is not None:
            for e in range(len(sep_list)):
                sep_list[e] = sep_list[e].replace(replace_old, replace_new)
        return sep_list        
    else:
        for e in range(len(data)):
            data[e] = data[e].replace(replace_old, replace_new)          
        return data

def count_dict(data): # zaehler-dict, wobei auf 0 als value fuer alle keys initialisiert ist
    command_count_dict = {i : 0 for i in range(len(data))}

    return command_count_dict    

def command_runner_part1(data, count_dict):
    i = 0
    acc = 0
    loop_indices = []
    while True:
        splitted_line = data[i].split()
        if "nop" in data[i] and count_dict[i] == 0:
            count_dict[i] = count_dict[i] + 1
            loop_indices.append(i)
            i += 1
        elif "acc" in data[i] and count_dict[i] == 0:
            acc += int(splitted_line[1])
            count_dict[i] = count_dict[i] + 1
            loop_indices.append(i)
            i += 1
        elif "jmp" in data[i] and count_dict[i] == 0:
            count_dict[i] = count_dict[i] + 1
            loop_indices.append(i)
            i += int(splitted_line[1]) # jump nach vorne oder zurueck
        else:
            break       
    return count_dict, acc, loop_indices

def find_exitpoints(data):
    jumpout = 1
    count_exitpoints = 0
    exitpoints = []
    for i in range(len(data)-1, -1, -1): # von hinten runter, da exitpoints am ende sind
        splittet_line = data[i].split()
        if splittet_line[0] == "acc":
            exitpoints.append(i)
            # print(data[i] + "ist Ausstiegspunkt")
            count_exitpoints += 1
        elif splittet_line[0] == "jmp" and splittet_line[1] == "+" + str(jumpout): # jmp's muessen als Bedingung ans Ende springen koennen
            exitpoints.append(i)
            # print(data[i] + "\nist Ausstiegspunkt")
            count_exitpoints += 1
        elif splittet_line[0] == "nop":
            exitpoints.append(i)
            # print(data[i] + "ist Ausstiegspunkt")
            count_exitpoints += 1
        else:
            break    
        jumpout += 1
    return exitpoints      
# please improve command_runner_part2 or exit_point_connect, there is still something missing
def command_runner_part2(data, count_dict):
    j = 0
    acc = 0
    while j < len(data):
        splitted_line = data[j].split()
        if "nop" in data[j] and count_dict[j] == 0:
            count_dict[j] = count_dict[j] + 1
            print(j)
            j += 1
            print(j)
        elif "acc" in data[j] and count_dict[j] == 0:
            acc += int(splitted_line[1])
            count_dict[j] = count_dict[j] + 1
            j += 1
            print(j)
        elif "jmp" in data[j] and count_dict[j] == 0:
            count_dict[j] = count_dict[j] + 1
            j += int(splitted_line[1])
            print(j) 
        elif j == len(data)-1:
            print("This loop works")
            ende = True
            # j += 1
            # break
        else:
            ende = False
            break     

    return acc, ende

def exit_point_connect(data_list):
    zeros_dict = count_dict(data_list) # neues dict mit nur nullen als values
    used_and_unused_entries_dict = command_runner_part1(data_list, zeros_dict)[0] #part1 durchlaufen lassen um zu sehen welche commands ausserhalb der schleife liegen im dictionary
    exit_points = find_exitpoints(data_list) # Ausstiegspunkte wiedergeben als liste
    loop_indices = command_runner_part1(data_list, count_dict(data_list))[2] # zeros_dict geht hier aus irgendeinem Grund nicht
    nop_jmp_count = 0
    acc_count = 0
    for i in loop_indices:
        splitted_line = data_list[i].split() # erstmal in zwei eintraege aufsplitten
        if splitted_line[0] == "acc":
            pass
        elif splitted_line[0] == "nop" and (int(splitted_line[1]) + i) in exit_points:
            print("nop auf jmp aendern empfohlen")
        elif splitted_line[0] == "nop":
            # print(data_list[i] + " to")
            data_list[i] = "jmp " + splitted_line[1] # nop durch jmp ersetzen und probieren
            # print(data_list[i])
            print(command_runner_part2(data_list, count_dict(data_list)))
            data_list[i] = "nop " + splitted_line[1] # jmp wieder auf nop zuruecksetzen
        elif splitted_line[0] == "jmp":
            # print(data_list[i] + " to")
            data_list[i] = "nop " + splitted_line[1]
            # print(data_list[i])
            print(command_runner_part2(data_list, count_dict(data_list)))
            data_list[i] = "jmp " + splitted_line[1]
        # print(str((int(splitted_line[1]))) + " " + str(i) + " = " + str((int(splitted_line[1]) + i)))    

    loop_size = sum(1 for value in used_and_unused_entries_dict.values() if value == 1)

def main():
    data = read_data("advent_of_code_8.txt") # data ist auch schon eine liste
    data_list = listcreater(data, None, "\n", "") # mach ne liste ohne die "\n"'s die mit reingekommen sind
#-------------------part1---------------------#    
    # print(command_runner_part1(data_list, count_dict(data))[1])
#-------------------part2---------------------#
    print(exit_point_connect(data))


if __name__ == "__main__":
    main()        