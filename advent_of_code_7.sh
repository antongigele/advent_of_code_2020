# #!/bin/bash

# while read line || [ -n "$line" ] ;
#     do 
#         array[$i]="$line"
#         let i++ ;

#     done < advent_of_code_7.txt    
# for ((i=0;i<=20;i++))
#     do
#         for word in ${array[i]}
#             do
#                 echo ${word}
#             done    
#         # if [[ ${array[i]} == *"shiny gold bags"* ]]; then
#         #     num=$(($i + 1))
#         #     echo "There it is in line ${num}";
#         # fi
            
#     done
# k=0;
# for ((i=0;i<=${#array[@]};i++))
#     do  
#         if [[ ${array[$i]} == *"shiny gold bags"* ]]; then
#             shiny_gold_bag_arr[$k]="${array[$i]}"
#             let k++;
#         fi   
#     done   

# ( IFS=$'\n'; echo "${shiny_gold_bag_arr[*]}" ) # das array ausgeben
#--------------------------------------------------------------------------------
string="muted coral bags contain 1 vibrant teal bag, 5 dim tan bags, 4 light bronze bags." 
IFS=' ' read -r -a stringarray <<< "$string"

# for ((i=0;i<=${#stringarray[@]};i++))
#     do  
#         if [ $i -lt 3 ] || [ $i -gt 3 ]; then
#             echo "${stringarray[i]}"  
#         fi     
#     done

# for ((i=0;i<=${#stringarray[@]};i++))
#     do  
#         num=$(($i + 1))
#         if [ ${stringarray[$i]} == "shiny" ] && [ ${stringarray[$num]} == "gold" ]; then
#             break
#         elif [ $i -lt 3 ] || [ $i -gt 3 ]; then
#             echo "${stringarray[i]}"    
#         else 
#             echo "no useful entry"     
#         fi     
#     done 
for ((i=0;i<=${#stringarray[@]};i++))
    do  
        numplus=$(($i + 1))
        numplustwo=$(($i + 2))
        if [ ${stringarray[$i]} == "shiny" ] && [ ${stringarray[$numplus]} == "gold" ]; then
            break
        elif [ $i -lt 3 ] || [ $i -gt 3 ]; then
            # echo "${stringarray[$i]} ${stringarray[$numplus]}"
            valid_bags+=( "${stringarray[$i]} ${stringarray[$numplus]} ${stringarray[$numplustwo]}" ) 
        else 
            echo "no useful entry"     
        fi     
    done  

( IFS=$'\n'; echo "${valid_bags[*]}" )      