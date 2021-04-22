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
    //---------------------------part1---------------------------
    public static LinkedHashMap<Integer, String> create_dict(String[] input_array) {
        LinkedHashMap<Integer, String> dict = new LinkedHashMap<Integer, String>();
        for(int i = 0; i < input_array.length; i++) {
            dict.put(i, input_array[i]);
        }
        return dict;
    }
    // Die Funktion hat noch einen fehler
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
    public static ArrayList<Integer> array_to_int_arraylist(String[] input_array) {
        ArrayList<Integer> numbers_game = new ArrayList<Integer>();
        for (String s : input_array) {
            numbers_game.add(Integer.parseInt(s));
        }
        return numbers_game;
    } 
    public static void main(String[] args) {
        // File einlesen
        String string_data = readFileAsString("test_1.txt");

        // File-Werte in array umwandeln
        String[] input_array;
        input_array = stringToArray(string_data, ",");
        //---------------------------part1---------------------------
        // // Dictionary erstellen
        // LinkedHashMap<Integer, String> dictionary = create_dict(input_array);
        // System.out.println(dictionary);
        // LinkedHashMap<Integer, String> recursive = eval_last_entry(dictionary);
        // LinkedHashMap<Integer, String> recursive2 = eval_last_entry(recursive);
        // LinkedHashMapRecursion(0, 2020, dictionary);
        //---------------------------part2---------------------------
        ArrayList<Integer> numbers_game = new ArrayList<Integer>();
        numbers_game = array_to_int_arraylist(input_array);
        System.out.println(numbers_game);
        // System.gc(); garbage collector
        // int l = 0;
        // ArrayList<Integer> numbers = new ArrayList<Integer>();
        // for (int i = 0; i < 30000000; i++) {
        //     l = i + 2;
        //     numbers.add(l);
        // }
        // System.out.println(numbers.get(29000000));
    }
}