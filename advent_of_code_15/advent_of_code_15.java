import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

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

    public static Map progression_dict(String[] input_array) {

    }

    public static void main(String[] args) {
        String string_data = readFileAsString("test_1.txt");
        String[] input_array;
        input_array = stringToArray(string_data, ",");
        System.out.println(Arrays.toString(input_array)); // Arrays.toString Methode notwendig

    }
}