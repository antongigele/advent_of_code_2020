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
            dict.put(i, Integer.parseInt(input_array[i]));
        }
        return dict;
    }
    //---------------------------part1---------------------------
    public static LinkedHashMap<Integer, String> eval_last_entry(LinkedHashMap<Integer, String> input_dict) {
        // den letzten key-value-pair holen
        int last_key = 0;
        for (int key: input_dict.keySet()) {
            last_key = key;
        }
        String last_value = input_dict.get(last_key);
        // System.out.println(Integer.toString(last_key) + " " + last_value);
        
        LinkedHashMap<Integer, String> narrowed_input_dict = new LinkedHashMap<Integer, String>(input_dict); // kopie erstellen
        narrowed_input_dict.remove(last_key); // letzten eintrag aus der kopie löschen damit die kopie nach diesem dann durchsucht werden kann
        if (narrowed_input_dict.containsValue(last_value) == false) {
            input_dict.put(last_key+1, "0"); // erstmal schauen ob der value überhaupt vorkommt
        }
        else {
            for (Map.Entry<Integer, String>item : narrowed_input_dict.entrySet()) { // durch LinkedHashMap mit key-values iterieren

                if (item.getValue().equals(last_value) == true) {
                    int value = last_key - item.getKey();
                    input_dict.put(last_key+1, Integer.toString(value));
                    // input_dict.put(item.getKey(), "");
                    input_dict.remove(item.getKey()); // funktioniert aus irgendeinem Grund nicht
                    break;
                }
                else {
                    ;
                }
            }
        }
        return input_dict;
    }

    public static LinkedHashMap<Integer, String> LinkedHashMapRecursion(int counter, int ending_point, LinkedHashMap<Integer, String> dictionary) {
        counter++;
        if (counter < ending_point) {
            System.out.println(counter);
            LinkedHashMap<Integer, String> eval_dict = eval_last_entry(dictionary);
            try {
                return LinkedHashMapRecursion(counter, ending_point, eval_dict);
            }
            catch (Exception e) {
                System.out.println(e);
                return dictionary;
            }
        
        }
        else {
            System.out.println(dictionary.get(ending_point-1));
            return dictionary;
        }
    }
    //---------------------------part2---------------------------
    public static void eval_last_entry_2(LinkedHashMap<Integer, Integer> numbers_game, int last_index) {
        int last_val = numbers_game.get(last_index);
        numbers_game.remove(last_index);
        if (numbers_game.values().contains(last_val) == true) { // <<--------- langsam, vertausche key und value in der map, containskey ist O(1)!
            int prev_index = 0;
            // for (Map.Entry<Integer, Integer> entry : numbers_game.entrySet()) {
            //     if (entry.getValue().equals(last_val)) {
            //         prev_index = entry.getKey();
            //         break;
            //     }
            // }
            numbers_game.put(last_index, last_val);
            numbers_game.put(last_index+1, last_index-prev_index);
            numbers_game.remove(prev_index);
            // System.out.println(Integer.toString(last_index-prev_index) + " added to the end");
        }
        else {
            numbers_game.put(last_index, last_val);
            numbers_game.put(last_index+1, 0);
            // System.out.println("0 added to the end");
        }
    }

    public static int grow_list(LinkedHashMap<Integer, Integer> numbers_game, int nth_number) {
        for (int i = numbers_game.size()-1; i < nth_number; i++) {
            eval_last_entry_2(numbers_game, i);
        }
        // return numbers_game;
        return numbers_game.get(nth_number-1);
    }

    public static void main(String[] args) {
        // File einlesen
        String string_data = readFileAsString("test_1.txt");

        // File-Werte in array umwandeln
        String[] input_array;
        input_array = stringToArray(string_data, ",");
        //---------------------------part1---------------------------
        // Dictionary erstellen
        // LinkedHashMap<Integer, String> recursive = eval_last_entry(dictionary);
        // LinkedHashMap<Integer, String> recursive2 = eval_last_entry(recursive);
        // LinkedHashMapRecursion(0, 2020, dictionary);
        //---------------------------part2---------------------------
        LinkedHashMap<Integer, Integer> numbers_game = create_dict(input_array);
        eval_last_entry_2(numbers_game, 2);
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