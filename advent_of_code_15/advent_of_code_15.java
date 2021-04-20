import java.io.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileReader;
import java.io.IOException;
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

    public static HashMap<Integer, String> eval_last_entry(HashMap<Integer, String> input_dict) {
        String last_value = input_dict.get(input_dict.size());
        HashMap<Integer, String> narrowed_input_dict = input_dict;
        narrowed_input_dict.remove(input_dict.size()-1);
        if (input_dict.containsValue(last_value) == false) {
            input_dict.put(input_dict.size()+2, "0");
        }
        else {
                int j = 0;
            for(String i : narrowed_input_dict.values()) {
                System.out.println(i);
                if (i == last_value) {
                    System.out.println(narrowed_input_dict.get(j));
                }
                else {
                    System.out.println(j);
                    continue;
                }
                j++;
            }
        }
        return input_dict;
    }

    public static void main(String[] args) {
        // File einlesen
        String string_data = readFileAsString("test_1.txt");

        // File-Werte in array umwandeln
        String[] input_array;
        input_array = stringToArray(string_data, ",");

        // Dictionary erstellen
        HashMap<Integer, String> dictionary = create_dict(input_array);

        // System.out.println(create_dict(input_array).toString()); // toString Methode notwendig
        System.out.println(dictionary.toString());
        System.out.println(eval_last_entry(dictionary));
    }
}