# #!/bin/bash

while read line || [ -n "$line" ] ;
    do 
        array[$i]="$line"
        let i++ ;

    done < text.txt
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
c=0;
for ((i=0;i<=${#array[@]};i++))
    do  
        if [[ ${array[$i]} == *"shiny gold bag"* ]] ; then
            shiny_gold_bag_arr[$c]="${array[$i]}"
            let c++;
        fi   
    done   

# ( IFS=$'\n'; echo "${shiny_gold_bag_arr[*]}" ) # das array ausgeben
#--------------------------------------------------------------------------------
# string="muted coral bags contain 1 vibrant teal bag, 5 dim tan bags, 4 light bronze bags." 
# IFS=' ' read -r -a stringarray <<< "$string"

for ((i=0;i<=${#shiny_gold_bag_arr[@]};i++))
do
    k=0;
    IFS=' ' read -r -a stringarray <<< "${shiny_gold_bag_arr[$i]}"
    for ((j=0;j<=${#stringarray[@]};j++))
    do  
        numplus=$(($j + 1))
        numplustwo=$(($j + 2))
        if [[ ${stringarray[$j]} == "shiny" ]] && [[ ${stringarray[$numplus]} == "gold" ]]; then
            break
        else
            valid_bags+=( "${stringarray[$j]} ${stringarray[$numplus]} ${stringarray[$numplustwo]}" )      
        fi     
    done
    # ( IFS=$'\n'; echo "${valid_bags[*]}" )
    
    for ((l=0;l<=${#valid_bags[@]};l++))
        do  
            if [[ "${valid_bags[$l]}" == *"bags" ]] \
            || [[ "${valid_bags[$l]}" == *"bag" ]] \
            || [[ "${valid_bags[$l]}" == *"bags," ]] \
            || [[ "${valid_bags[$l]}" == *"bag," ]] \
            || [[ "${valid_bags[$l]}" == *"bags." ]] \
            || [[ "${valid_bags[$l]}" == *"bag." ]]; then
                valid_bags_cleaned[$k]="${valid_bags[$l]}"
                let k++;
            fi   
        done

done    
( IFS=$'\n'; echo "${valid_bags_cleaned[*]}" )
# ( IFS=$'\n'; echo "${valid_bags[*]}" )

# for ((i=0;i<=${#stringarray[@]};i++))
#     do  
#         numplus=$(($i + 1))
#         numplustwo=$(($i + 2))
#         if [[ ${stringarray[$i]} == "shiny" ]] && [[ ${stringarray[$numplus]} == "gold" ]]; then
#             break
#         else
#             # echo "${stringarray[$i]} ${stringarray[$numplus]}"
#             valid_bags+=( "${stringarray[$i]} ${stringarray[$numplus]} ${stringarray[$numplustwo]}" )      
#         fi     
#     done  

# ( IFS=$'\n'; echo "${valid_bags[*]}" )

# k=0;
# for ((i=0;i<=${#valid_bags[@]};i++))
#     do  
#         if [[ "${valid_bags[$i]}" == *"bags" ]] \
#         || [[ "${valid_bags[$i]}" == *"bag" ]] \
#         || [[ "${valid_bags[$i]}" == *"bags," ]] \
#         || [[ "${valid_bags[$i]}" == *"bag," ]] \
#         || [[ "${valid_bags[$i]}" == *"bags." ]] \
#         || [[ "${valid_bags[$i]}" == *"bag." ]]; then
#             valid_bags_cleaned[$k]="${valid_bags[$i]}"
#             let k++;
#         fi   
#     done

# ( IFS=$'\n'; echo "${valid_bags_cleaned[*]}" )