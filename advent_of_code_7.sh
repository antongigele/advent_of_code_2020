#!/bin/bash

while read line || [ -n "$line" ] ;
    do 
        line_array[$i]="$line"
        let i++ ;

    # done < advent_of_code_7.txt
    done < text.txt
# for ((i=0;i<=20;i++))
#     do
#         for word in ${line_array[i]}
#             do
#                 echo ${word}
#             done    
#         # if [[ ${line_array[i]} == *"shiny gold bags"* ]]; then
#         #     num=$(($i + 1))
#         #     echo "There it is in line ${num}";
#         # fi
#     done
c=0;
for ((i=0;i<=${#line_array[@]};i++))
    do  
        if [[ ${line_array[$i]} == *"shiny gold bag"* ]] ; then # schauen ob zeile "shiny gold bag" enthält
            shiny_gold_bag_arr[$c]="${line_array[$i]}"
            let c++;
        fi   
    done   

# ( IFS=$'\n'; echo "${shiny_gold_bag_arr[*]}" ) # das array ausgeben
#--------------------------------------------------------------------------------
# string="muted coral bags contain 1 vibrant teal bag, 5 dim tan bags, 4 light bronze bags." 
# IFS=' ' read -r -a stringarray <<< "$string"

# array mit den richtigen Taschen erstellen
for ((i=0;i<=${#shiny_gold_bag_arr[@]};i++))
do
    IFS=' ' read -r -a stringarray <<< "${shiny_gold_bag_arr[$i]}"
    if [[ ${stringarray[1]} == "gold" ]]; then
        echo "shiny gold bags cannot hold shiny gold bags"
    else        
        valid_bags+=( "${stringarray[0]} ${stringarray[1]} ${stringarray[2]}" )
    fi    
#    
    # for ((l=0;l<=${#valid_bags[@]};l++))
    #     do  
    #         if [[ "${valid_bags[$l]}" == *"bags" ]] \
    #         || [[ "${valid_bags[$l]}" == *"bag" ]] \
    #         || [[ "${valid_bags[$l]}" == *"bags," ]] \
    #         || [[ "${valid_bags[$l]}" == *"bag," ]] \
    #         || [[ "${valid_bags[$l]}" == *"bags." ]] \
    #         || [[ "${valid_bags[$l]}" == *"bag." ]]; then
    #             valid_bags_cleaned[$k]="${valid_bags[$l]}"
    #             let k++;
    #         fi   
    #     done
done    
( IFS=$'\n'; echo "${valid_bags[*]}" )
# "." "," und "s" müssen vom ende entfernt werden
for ((l=0;l<=${#valid_bags[@]};l++))
do  
    if [[ "${valid_bags[l]: -1}" == "s" ]] \
    || [[ "${valid_bags[l]: -1}" == "," ]] \
    || [[ "${valid_bags[l]: -1}" == "." ]]; then
        valid_bags_cleaned[$l]="${valid_bags_cleaned[l]:: -1}";
        # echo "${valid_bags_cleaned[l]}"
    fi    
done
# den loop zweimal laufen lassen damit auch die "s" vor dem "," oder "." entfernt werden
for ((l=0;l<=${#valid_bags[@]};l++))
do  
    if [[ "${valid_bags[l]: -1}" == "s" ]] \
    || [[ "${valid_bags[l]: -1}" == "," ]] \
    || [[ "${valid_bags[l]: -1}" == "." ]]; then
        valid_bags[$l]="${valid_bags[l]:: -1}";
    fi    
done   
( IFS=$'\n'; echo "${valid_bags[*]}" )

valid_counter=0;
# zähl wo überall shiny gold bags reinkommen können
for ((l=0;l<${#valid_bags[@]};l++))
do
    key_regex="${valid_bags[l]}";
    for ((k=0;k<${#line_array[@]};k++))
    do
        if [[ "${line_array[k]}" == *"$key_regex"* ]]; then
            let valid_counter++;
            echo "key_regex detected"
            line_array[k]="This array-entry has been deleted";
        fi
    done
done

echo $valid_counter
# ( IFS=$'\n'; echo "${valid_bags_cleaned[*]}" ) > output.txt
# ( IFS=$'\n'; echo "${line_array[*]}" )