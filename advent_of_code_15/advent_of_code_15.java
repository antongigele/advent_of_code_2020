import java.io.*;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.*;

public class advent_of_code_15 {

    public static String readFileAsString(String path) {
        File input_file = new File(path);
        try {
            Scanner reader = new Scanner(input_file);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                return data;
            
            }
            reader.close();
        } 
        catch (FileNotFoundException e) {
            e.printStackTrace();
            return "File not found";
        }
        return "0";
    }

    public static String[] stringToArray(String str, String sep) {
        String[] str_arr = str.split(sep);
        return str_arr;
    }

    public static LinkedHashMap<Integer, Integer> create_dict(String[] input_array) {
        LinkedHashMap<Integer, Integer> dict = new LinkedHashMap<Integer, Integer>();
        for(int i = 0; i < input_array.length; i++) {
            dict.put(Integer.parseInt(input_array[i]), i);
        }
        return dict;
    }

    //----------------------------Solution-------------------------------
    // hier weitermachen ----->
    public static void eval_last_entry_2(int last_index, LinkedHashMap<Integer, Integer> numbers_game) {
        int last = numbers_game.get(last_index);
        numbers_game.remove(last_index);
        if (numbers_game.values().contains(last) == true) { // <<--------- langsam, vertausche key und value in der map, containskey ist O(1)!
            int prev_index = 0;
            // for (Map.Entry<Integer, Integer> entry : numbers_game.entrySet()) {
            //     if (entry.getValue().equals(last_val)) {
            //         prev_index = entry.getKey();
            //         break;
            //     }
            // }
            numbers_game.put(last_index, last);
            numbers_game.put(last_index+1, last_index-prev_index);
            numbers_game.remove(prev_index);
            // System.out.println(Integer.toString(last_index-prev_index) + " added to the end");
        }
        else {
            numbers_game.put(last_index, last);
            numbers_game.put(last_index+1, 0);
            // System.out.println("0 added to the end");
        }
    }

    public static int grow_list(LinkedHashMap<Integer, Integer> numbers_game, int nth_number) {
        for (int i = numbers_game.size()-1; i < nth_number; i++) {
            eval_last_entry_2(i, numbers_game);
        }
        // return numbers_game;
        return numbers_game.get(nth_number-1);
    }

    public static void main(String[] args) {
        // // File einlesen
        // String string_data = readFileAsString("test_1.txt");

        // // File-Werte in array umwandeln
        // String[] input_array;
        // input_array = stringToArray(string_data, ",");
        // Map<Integer, Integer> numbers_game = create_dict(input_array);
        // System.out.println(numbers_game);

    
        // eval_last_entry_2(2, numbers_game);
        // eval_last_entry_2(numbers_game, 3);
        // eval_last_entry_2(numbers_game, 4);
        // eval_last_entry_2(numbers_game, 5);
        // eval_last_entry_2(numbers_game, 6);
        // System.out.println(numbers_game);
        
        // long startTime = System.nanoTime();
        // System.out.println(grow_list(numbers_game, 30 * 1000 *10));
        // long endTime = System.nanoTime();
        // long timeElapsed = endTime - startTime;
        // double sek = timeElapsed/1000000;
        // System.out.println(sek);
    }
}