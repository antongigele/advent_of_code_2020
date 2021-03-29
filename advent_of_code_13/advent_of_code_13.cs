using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace advent_of_code_13 {
    
    class advent_of_code_13 {

        // function gibt ein tuple = (array, float) zurück
        public static (string[], float) ReadFromFile(string path, string sep = ",") {

            string[] lines = System.IO.File.ReadAllLines(@path);
            float departure_timestamp = Int32.Parse(lines[0]);

            // create das bus array mit einem separator mit der split-methode
            string separator = sep;
            string[] bus_list = lines[1].Split(separator);

            return(bus_list, departure_timestamp);
        }

        public static int Non_x_Entries_Len(string[] bus_list) {
            int len = 0;
            //anzahl der einträge die nicht x sind
            foreach (string e in bus_list) {
                if (e != "x") {
                    len++;
                }
            }
            return len;
        }

//---------------------------------part1----------------------------------
        public static double[] residue_distance(string[] bus_list, float departure_timestamp) {
            double[] residues = new double[bus_list.Length];
            int i = 0;
            foreach (string e in bus_list) {
                if (e == "x") { // ignoriere die x-Einträge
                    residues[i] = 0;
                }
                else { // dividiere den ersten möglichen abfahrtszeitpunkt durch bus_ids = bus_intervalle und nimm davon nur den betrag der (reste - 1)
                    residues[i] = 1 - (departure_timestamp/float.Parse(e) - Math.Floor(departure_timestamp/float.Parse(e)));
                    residues[i] *= double.Parse(bus_list[i]); // multipliziere sie mit den bus_ids
                    residues[i] = Math.Round(residues[i]);
                }
                i++;
            }
            return residues;
        }

        public static int calculate_min(double[] residues, string[] bus_list) {
            
            var non_x_entries_len = Non_x_Entries_Len(bus_list);

            int[] waiting_times = new int[non_x_entries_len];
            int[] bus_ids = new int[non_x_entries_len];
            int w = 0;
            int b = 0;
            for (int i = 0; i < residues.Length; i++) {
                if (residues[i] != 0) {
                    waiting_times[w] = (int)residues[i];
                    w++;
                    bus_ids[b] = int.Parse(bus_list[i]);
                    b++;
                }
            }
            int min = waiting_times.Min();
            int related_bus_id = bus_ids[Array.IndexOf(waiting_times, min)];
            return related_bus_id*min;
        }

//---------------------------------part2----------------------------------
        public static (int[], int[]) congruences(string[] bus_list) {
            var non_x_entries_len = Non_x_Entries_Len(bus_list);

            int[] rests = new int[non_x_entries_len];
            int[] moduli = new int[non_x_entries_len];
            int r = 0;
            int m = 0;
            for (int i = 0; i < bus_list.Length; i++) {
                if (bus_list[i] != "x") {
                    rests[r] = i;
                    r++;
                    moduli[m] = int.Parse(bus_list[i]);
                    m++;
                }
            }
            return(rests, moduli);
        }

        public static int gcd(int num1, int num2) {
            if (num1 <= 0 || num2 <= 0) {
                return 0;
            }
            else {
                while (num1 != 0 && num2 != 0){
                    if (num1 > num2) {
                        num1 %= num2;
                    }
                    else {
                        num2 %= num1;
                    }
                }
                return num1 | num2;
            }
        }

        public static double modInverse(double num, double mod) {
            if (gcd((int)num,  (int)mod) != 1) { // die zahlen müssen teilerfremd sein
                return 0;
            }
            double i = 1;
            bool x_is_int = false;
            while (x_is_int == false) {
                
                double x = (i*mod + 1)/num;
                if (x == Math.Round(x, 0)) {
                    x_is_int = true;
                    return x;
                }
                else {
                    i++;
                }
            }
            return 0;
        }

        public static double solve_modulo_eqs() {
            return 0;
        }

//----------------------------main-methode--------------------------------
        public static void Main() {
            (string[] bus_list, float departure_timestamp) = ReadFromFile("advent_of_code_13.txt"); // der output dieser funktion ist ein tuple
//---------------------------------part1----------------------------------            
            // var residues = residue_distance(bus_list, departure_timestamp); // der zeitliche abstand wird als rest kalkuliert
            
            //Console.WriteLine(calculate_min(residues, bus_list));
//---------------------------------part2----------------------------------
            (int[] rests, int[] moduli) = congruences(bus_list);
            for (int i = 0; i < rests.Length; i++) {
                Console.WriteLine("x = " + rests[i] + " mod " + moduli[i]);
            }



            // Console.WriteLine(gcd(37, 587));
            // Console.WriteLine(modInverse(8, 25));
            // Console.WriteLine(modInverse(3, 11));
            // Console.WriteLine(modInverse(13, 7));
            // Console.WriteLine(modInverse(4, 12));
//---------------------------------test----------------------------------
        }
    }

}