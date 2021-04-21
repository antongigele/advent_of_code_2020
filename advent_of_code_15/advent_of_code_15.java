import java.io.*;
import java.io.FileNotFoundException;
import java.util.Scanner;
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

    public static HashMap<Integer, String> create_dict(String[] input_array) {
        HashMap<Integer, String> dict = new HashMap<Integer, String>();
        for(int i = 0; i < input_array.length; i++) {
            dict.put(i, input_array[i]);
        }
        return dict;
    }
    // Die Funktion hat noch einen fehler
    public static HashMap<Integer, String> eval_last_entry(HashMap<Integer, String> input_dict) {
        // den letzten key-value-pair holen
        int last_key = 0;
        for (int key: input_dict.keySet()) {
            last_key = key;
        }
        String last_value = input_dict.get(last_key);
        // System.out.println(Integer.toString(last_key) + " " + last_value);
        
        HashMap<Integer, String> narrowed_input_dict = new HashMap<Integer, String>(input_dict); // kopie erstellen
        narrowed_input_dict.remove(last_key); // letzten eintrag aus der kopie löschen damit die kopie nach diesem dann durchsucht werden kann
        if (narrowed_input_dict.containsValue(last_value) == false) {
            input_dict.put(last_key+1, "0"); // erstmal schauen ob der value überhaupt vorkommt
        }
        else {
            for (HashMap.Entry<Integer, String>item : narrowed_input_dict.entrySet()) { // durch hashmap mit key-values iterieren

                if (item.getValue().equals(last_value) == true) {
                    int value = last_key - item.getKey(); // <--- guter trick! funktioniert hier aber nicht. der last_value hat in diesem fall immer die größe-1 als key
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

    public static HashMap<Integer, String> HashMapRecursion(int ending_point, HashMap<Integer, String> dictionary) {
        if (dictionary.size() < ending_point) {
            HashMap<Integer, String> eval_dict = eval_last_entry(dictionary);
            return HashMapRecursion(ending_point, eval_dict);
        }
        else {
            System.out.println(dictionary.get(ending_point-1));
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
        // System.out.println(dictionary);
        // Rekursion notwendig
        // HashMap<Integer, String> recursive = eval_last_entry(dictionary);
        // HashMap<Integer, String> recursive2 = eval_last_entry(recursive);
        // HashMap<Integer, String> recursive3 = eval_last_entry(recursive2);
        // HashMap<Integer, String> recursive4 = eval_last_entry(recursive3);
        // HashMap<Integer, String> recursive5 = eval_last_entry(recursive4);
        // System.out.println(recursive5);
        // recursive5.remove(0);
        // recursive5.remove(1);
        // recursive5.remove(4);
        // System.out.println(recursive5);
        // HashMap<Integer, String> recursive6 = eval_last_entry(recursive5);
        // HashMap<Integer, String> recursive7 = eval_last_entry(recursive6);
        // System.out.println(recursive6);
        // System.out.println(eval_last_entry(recursive2));
        System.out.println(HashMapRecursion(70, dictionary));

    }
}