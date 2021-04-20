import java.io.*;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;
import java.util.HashMap;

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
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return "File not found";
        }
        return "0";
    }

    public static String[] stringToArray(String str, String sep) {
        String[] str_arr = str.split(sep);
        return str_arr;
    }

    public static HashMap<Integer, String> create_dict(String[] input_array) {
        HashMap<Integer, String> dict = new HashMap<Integer, String>();
        for(int i = 0; i < input_array.length; i++) {
            dict.put(i, input_array[i]);
        }
        return dict;
    }
    // Die Funktion ist noch nicht vollständig
    public static HashMap<Integer, String> eval_last_entry(HashMap<Integer, String> input_dict) {
        String last_value = input_dict.get(input_dict.size()-1);
        HashMap<Integer, String> narrowed_input_dict = new HashMap<Integer, String>(input_dict); // kopie erstellen
        narrowed_input_dict.remove(input_dict.size()-1); // letzten eintrag aus der kopie löschen damit die kopie nach diesem dann durchsucht werden kann
        if (narrowed_input_dict.containsValue(last_value) == false) {
            input_dict.put(input_dict.size(), "0"); // erstmal schauen ob der value überhaupt vorkommt
        }
        else {
            for(HashMap.Entry<Integer, String>item : narrowed_input_dict.entrySet()) { // durch hashmap mit key-values iterieren

                if (item.getValue().equals(last_value) == true) {
                    int value = input_dict.size()-1 - item.getKey(); // der last_value hat in diesem fall immer die größe-1 als key
                    input_dict.put(input_dict.size(), Integer.toString(value));
                }
                else {
                    ;
                }
            }
        }
        return input_dict;
    }

    public static HashMap<Integer, String> HashMapRecursion(int ending_point, HashMap<Integer, String> dictionary) {
        if (dictionary.size() < ending_point) {
            HashMap<Integer, String> eval_dict = eval_last_entry(dictionary);
            return HashMapRecursion(ending_point, eval_dict);
        }
        else {
            System.out.println(dictionary.get(ending_point));
            return dictionary;
        }
    }

    public static void main(String[] args) {
        // File einlesen
        String string_data = readFileAsString("test_1.txt");

        // File-Werte in array umwandeln
        String[] input_array;
        input_array = stringToArray(string_data, ",");

        // Dictionary erstellen
        HashMap<Integer, String> dictionary = create_dict(input_array);

        // Rekursion notwendig
        // HashMap<Integer, String> recursive = new HashMap<Integer, String>(eval_last_entry(dictionary));
        // HashMap<Integer, String> recursive2 = eval_last_entry(recursive);
        // System.out.println(eval_last_entry(recursive2));
        System.out.println(HashMapRecursion(2020, dictionary));

    }
}