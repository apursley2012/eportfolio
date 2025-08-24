####################################################################
#  corner_grocer.py                                                                                                                                   #
#  Name: Alysha Pursley                                                                                                                                       #
#  Date: July 2025                                                                                                                                            #
#    Enhancement Two: corner_grocer_main.py                                                                                           #
#    Adds sort A–Z, sort by frequency, item search, and file export optionst o save                      #
#     frequency list and histogram. Uses helper functions in grocery_utils.py for sorting               #
#    and searching operations.                                                                                                                            #
####################################################################

####################################################################
#  Module Imports (C++ Equivalents)                                                                                                              #
#  collections.defaultdict replaces C++ std::map<int>                                                                               #
#  sys provides exit control like exit(0) in C++                                                                                              #
####################################################################
import sys
from collections import defaultdict
import grocery_utils as utils

####################################################################
#  GroceryFrequency Class                                                                                                                                #
#  Encapsulates item counting, printing, searching, and backups                                                         #
####################################################################
class GroceryFrequency:
    def __init__(self):
        #################################################################
        #  Initializes internal dictionary for frequency storage                                                                       #
        #  Equivalent to std::map<std::string, int> in C++                                                                                #
        #################################################################
        self.frequency = defaultdict(int)

    def process_input_file(self, filename):
        #################################################################
        #  Reads items from input file and populates frequency dictionary                                               #
        #  Equivalent to reading file and incrementing map values in C++                                                   #
        #################################################################
        try:
            with open(filename, 'r') as file:
                for line in file:
                    item = line.strip().lower()
                    if item:
                        self.frequency[item] += 1
        except FileNotFoundError:
            ################################################################
            #  File Not Found Exception                                                                                                                   #
            #  Equivalent to checking ifstream.fail() in C++                                                                                #
            ################################################################
            print(f"Error: File '{filename}' not found.")
            sys.exit(1)

    def lookup_item_frequency(self, item):
        #################################################################
        #  Returns item frequency (0 if not found)                                                                                           #
        #  Equivalent to map.find() logic in C++                                                                                                  #
        #################################################################
        return self.frequency.get(item.lower(), 0)

    def print_all_frequencies(self):
        #################################################################
        #  Prints all items and their frequencies                                                                                                   #
        #  Equivalent to iterating through std::map in C++                                                                              #
        #################################################################
        for item in sorted(self.frequency.keys()):
            print(f"{item}: {self.frequency[item]}")

    def print_histogram(self):
        #################################################################
        #  Prints each item with asterisk histogram based on count                                                             #
        #  Equivalent to printing item name and stars in C++                                                                          #            
        #################################################################
        for item in sorted(self.frequency.keys()):
            count = self.frequency[item]
            print(f"{item}: {'*' * count}")

####################################################################
#  Input Validation Function                                                                                                                               #
#  Ensures valid menu choice (1-9) and prevents crashes                                                                        #
####################################################################
def get_validated_choice():
    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 9:
            return choice
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 9.")
        return 0

####################################################################
#  Item Name Validation                                                                                                                                        #
#  Allows letters and spaces only                                                                                                                      #
####################################################################
def is_valid_item_name(item_name):
    return all(ch.isalpha() or ch.isspace() for ch in item_name)

####################################################################
#  Menu Display Function                                                                                                                                   #
#  Prints all menu options                                                                                                                                     #
####################################################################
def print_menu():
    print("\n========== Corner Grocer Menu ==========")
    print("1. Look up item frequency")
    print("2. Print all items and frequencies")
    print("3. Print frequency histogram")
    print("4. Sort items alphabetically (A–Z)")
    print("5. Sort items by frequency (high → low)")
    print("6. Search for a specific item")
    print("7. Save frequency list to frequency_list.dat")
    print("8. Save histogram to frequency_histogram.dat")
    print("9. Exit program")
    sys.stdout.flush()

####################################################################
#  Main Program                                                                                                                                                    #
#  Enhancement Two entry point                                                                                                                     #
####################################################################
if __name__ == "__main__":
    INPUT_FILE = "grocery_input.txt"   # keep consistent with Enhancement One

    grocery = GroceryFrequency()
    grocery.process_input_file(INPUT_FILE)

    
    running = True
    while running:
        print_menu()
        choice = get_validated_choice()

        if choice == 1:
            item = input("Enter item name: ").strip()
            if not item:
                print("Please enter a non-empty item name.")
                continue
            if not is_valid_item_name(item):
                print("Invalid item name. Use letters and spaces only.")
                continue
            freq = grocery.lookup_item_frequency(item)
            print(f"{item} was purchased {freq} time(s).")

        elif choice == 2:
            print("\nAll item frequencies:")
            grocery.print_all_frequencies()

        elif choice == 3:
            print("\nItem frequency histogram:")
            grocery.print_histogram()

        elif choice == 4:
            print("\nItems sorted alphabetically (A–Z):")
            utils.sort_alpha(grocery.frequency)

        elif choice == 5:
            print("\nItems sorted by frequency (high → low):")
            utils.sort_by_freq(grocery.frequency)

        elif choice == 6:
            query = input("Enter item to search: ").strip()
            if not query:
                print("Please enter a non-empty item name.")
                continue
            if not is_valid_item_name(query):
                print("Invalid item name. Use letters and spaces only.")
                continue
            utils.search_item(grocery.frequency, query)

        elif choice == 7:
            ################################################################
            #  Save Frequency List to file (last two options before exit)                                                        #
            #  Writes 'item count' per line to frequency_list.dat                                                                         #
            ################################################################
            try:
                with open("frequency_list.txt", "w", encoding="utf-8") as f:
                    for item in sorted(grocery.frequency.keys()):
                        f.write(f"{item} {grocery.frequency[item]}\n")
                print("Saved to frequency_list.dat")
            except Exception as e:
                print(f"Failed to save frequency list: {e}")

        elif choice == 8:
            ################################################################
            #  Save Histogram to file (last two options before exit)                                                                #
            #  Writes 'item: *****' lines to frequency_histogram.dat                                                                 #
            ################################################################
            try:
                with open("frequency_histogram.txt, "w", encoding="utf-8") as f:
                    # Sort by frequency (high → low), then A–Z for ties
                    for item, count in sorted(
                        grocery.frequency.items(),
                        key=lambda kv: (-kv[1], kv[0])
                    ):
                        f.write(f"{item}: {'*' * count}\n")
                print("Saved to frequency_histogram.dat")
            except Exception as e:
                print(f"Failed to save histogram: {e}")

        elif choice == 9:
            print("Goodbye!")
            running = False
