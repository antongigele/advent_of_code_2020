import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileReader;
import java.io.IOException;
public class advent_of_code_15 {

    // public static String readFileAsString(String path) {
    //     String text = "";
    // try {
    //   text = new String(Files.readAllBytes(Paths.get(path)));
    // } catch (IOException e) {
    //   e.printStackTrace();
    // }

    // return text;
    // }

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

    public static String[] stringToArray(String str) {
        String[] str_arr = str.split(",",3);
        return str_arr;
    }

    public static void main(String[] args) {
        String str = readFileAsString("test_1.txt");
        String[] input_array = stringToArray(str);
        System.out.println(input_array);
    }
}