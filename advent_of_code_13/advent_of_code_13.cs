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
            int len = 0;
            //anzahl der einträge die nicht x sind
            foreach (double e in residues) {
                if (e != 0) {
                    len++;
                }
            }
            int[] waiting_times = new int[len];
            int[] bus_ids = new int[len];
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


//----------------------------main-methode--------------------------------

        public static void Main() {
            (string[] bus_list, float departure_timestamp) = ReadFromFile("advent_of_code_13.txt"); // der output dieser funktion ist ein tuple
            var residues = residue_distance(bus_list, departure_timestamp); // der zeitliche abstand wird als rest kalkuliert

            Console.WriteLine(calculate_min(residues, bus_list));
        }
    }

}