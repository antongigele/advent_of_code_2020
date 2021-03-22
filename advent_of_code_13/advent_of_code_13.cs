using System;
using System.IO;

namespace advent_of_code_13 {
    
    class advent_of_code_13_part1 {

        public static void Main() {
            // System.Console.WriteLine(departure_timestamp);
            (string[] bus_list, float departure_timestamp) = ReadFromFile("advent_of_code_13.txt");
            var residues = residue_distance(bus_list, departure_timestamp);
            foreach (double e in residues) {
                Console.WriteLine(e + "\n");
            }
        }

        // function gibt ein tuple = (array, float) zurück
        public static (string[], float) ReadFromFile(string path, string sep = ",") {

            string[] lines = System.IO.File.ReadAllLines(@path);
            float departure_timestamp = Int32.Parse(lines[0]);

            // create the bus array with a separator using the split-method
            string separator = sep;
            string[] bus_list = lines[1].Split(separator);

            // var bus_tuple = new Tuple<float[], float>(bus_list, departure_timestamp);
            return(bus_list, departure_timestamp);
        }

        public static double[] residue_distance(string[] bus_list, float departure_timestamp) {
            double[] residues = new double[bus_list.Length];
            int i = 0;
            foreach (string e in bus_list) {
                if (e == "x") 
                {
                    Console.WriteLine(e + "\n");
                    residues[i] = 1;
                }
                else 
                {   
                    Console.WriteLine(departure_timestamp/float.Parse(e) - Math.Floor(departure_timestamp/float.Parse(e)) + "\n");
                    residues[i] = departure_timestamp/float.Parse(e) - Math.Floor(departure_timestamp/float.Parse(e));
                    residues[i] *= double.Parse(bus_list[i]);
                }
                i++;
            }
            return residues;
        }
        
    }

}