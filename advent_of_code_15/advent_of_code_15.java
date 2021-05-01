import java.io.*;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.concurrent.RejectedExecutionHandler;
import java.util.*;

public class advent_of_code_15 {

    public static String readFileAsString(String path) {
        File input_file = new File(path);
        Scanner reader = null;
        try {
            reader = new Scanner(input_file);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                return data;

            }
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return "File not found";
        }
        finally {
            if (reader != null) {
                reader.close();
            }
        }    
        return "0";
    }

    public static String[] stringToArray(String str, String sep) {
        String[] str_arr = str.split(sep);
        return str_arr;
    }

    public static ArrayList<Integer> array_to_int_arraylist(String[] input_array) {
        ArrayList<Integer> array_list = new ArrayList<Integer>();
        for (String s : input_array) {
            array_list.add(Integer.parseInt(s));
        }
        return array_list;
    }

    public static LinkedHashMap<Integer, Integer> create_dict(String[] input_array) {
        LinkedHashMap<Integer, Integer> dict = new LinkedHashMap<Integer, Integer>();
        for (int i = 0; i < input_array.length; i++) {
            dict.put(Integer.parseInt(input_array[i]), i);
        }
        return dict;
    }

    public static int get_nth_number(int nth_number, ArrayList<Integer> input_arraylist,
            Map<Integer, Integer> numbers_game) {
        int input_size = input_arraylist.size();
        int lastNumber = input_arraylist.get(input_size - 1);

        for (int i = input_size; i <= nth_number - 1; i++) {
            int newNumber = 0;
            if (numbers_game.containsKey(lastNumber)) {
                newNumber = i - 1 - numbers_game.get(lastNumber);
            }
            numbers_game.put(lastNumber, i - 1); // man schreibt hier immer die zahl der vorherigen runde auf, nach dem
                                                 // for-loop macht einen großen unterschied, da das noch nicht
                                                 // veränderte hashmap durchsucht werden kann
            lastNumber = newNumber;
        }

        return lastNumber;
    }

    public static void main(String[] args) {
        // File einlesen
        String string_data = readFileAsString("advent_of_code_15.txt");

        // File-Werte in array umwandeln
        String[] input_array;
        input_array = stringToArray(string_data, ",");
        ArrayList<Integer> input_arraylist = new ArrayList<Integer>();
        input_arraylist = array_to_int_arraylist(input_array);
        Map<Integer, Integer> numbers_game = create_dict(input_array);
        System.out.println(get_nth_number(30 * 1000 * 1000, input_arraylist, numbers_game));

    }
}