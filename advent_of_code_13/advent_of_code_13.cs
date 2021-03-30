using System;
using System.IO;
using System.Linq;

namespace advent_of_code_13 {
    
    class advent_of_code_13 {
        
        public static int count_Lines(string path) {
            var lineCount = 0;
            using (var reader = File.OpenText(@path)) {
                while (reader.ReadLine() != null) {
                    lineCount++;
                }
            }
            return lineCount;
        }

        // function gibt ein tuple = (array, float) zurück
        public static (string[], float) ReadFromFile(string path, string sep = ",") {
            string[] lines = System.IO.File.ReadAllLines(@path);
            
            if (count_Lines(path) == 2) {
                float departure_timestamp = Int32.Parse(lines[0]);

                // create das bus array mit einem separator mit der split-methode
                string separator = sep;
                string[] bus_list = lines[1].Split(separator);

                return(bus_list, departure_timestamp);
            }
            else {
                string separator = sep;
                string[] bus_list = lines[0].Split(separator);

                return(bus_list, 0);
            }

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

        public static long gcd(long num1, long num2) {
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
        //-------Nicht skalierbare Lösung des Inversenproblems-------
        // public static double modInverse(double num, double mod) {
        //     if (gcd((long)num,  (long)mod) != 1) { // die zahlen müssen teilerfremd sein
        //         Console.WriteLine("Numbers must be coprime");
        //         return 0;
        //     }
        //     double i = 1;
        //     bool x_is_int = false;
        //     while (x_is_int == false) {
                
        //         double x = (i*mod + 1); 
        //         // x = x/num; // <--- sehr rechenaufwändig! nicht scalable!
        //         if (x) {
        //             x_is_int = true;
        //             return x;
        //         }
        //         else {
        //             i++;
        //         }
        //     }
        //     Console.WriteLine(i);
        //     return 0;
        // }

        public static long modInverse(long a, long b) {
            if (gcd((long)a,  (long)b) != 1) { // die zahlen müssen teilerfremd sein
                Console.WriteLine("Numbers must be coprime");
                return 0;
            }
            // initialisierung der startwerte
            long u = 1;
            long v = 0; 
            long s = 0; 
            long t = 1;
            long mod = (long)b;
            while (b != 0) {
                long a_before = a; // muss sein, da variablen-assignment syntax wie in python auf einer zeile nicht möglich ist
                long u_before = u;
                long v_before = v;

                long q = a / b;
                a = b; // da a neu assignt wird, muss in der nächsten zeile das alte a her, gilt auch für u und v
                b = a_before - q*b;
                u = s;
                s = u_before - q*s;
                v = t;
                t = v_before - q*t;
            }
            if (u < 0) {
                return u + mod;
            }
            else {
                
                return u;
            }
        }

        public static double solve_modulo_eqs(int[] rests, int[] moduli) {
            long M = 1;
            long[] b_i_array = new long[moduli.Length];
            long[] b_i_inverse_array = new long[moduli.Length];
            for (int i = 0; i < moduli.Length; i++) {
                M *= moduli[i]; // berechne M als produkt aller moduli
            }
            for (int i = 0; i < moduli.Length; i++) {
                b_i_array[i] = M/moduli[i]; // berechne einzelne b_i's
            }
            for (int i = 0; i < moduli.Length; i++) {
                b_i_inverse_array[i] = modInverse(b_i_array[i], moduli[i]); // berechne einzelne jeweilige inverse zu den b_i's
            }
            long sum = 0;
            for (int i = 0; i < moduli.Length; i++) {
                sum += rests[i]*b_i_array[i]*b_i_inverse_array[i];
            }
            long result = sum % M; // ergebnis mod M
            return M - result; // nimm das komplement von result als lösung für den frühesten timestamp
        }

//----------------------------main-methode--------------------------------
        public static void Main() {
            (string[] bus_list, float departure_timestamp) = ReadFromFile("advent_of_code_13.txt"); // der output dieser funktion ist ein tuple
//---------------------------------part1----------------------------------            
            var residues = residue_distance(bus_list, departure_timestamp); // der zeitliche abstand wird als rest kalkuliert
            
            Console.WriteLine(calculate_min(residues, bus_list));
//---------------------------------part2----------------------------------
            (int[] rests, int[] moduli) = congruences(bus_list);
            for (int i = 0; i < rests.Length; i++) {
                Console.WriteLine("x = " + rests[i] + " mod " + moduli[i]);
            }
            Console.WriteLine(solve_modulo_eqs(rests, moduli));
        }
    }

}