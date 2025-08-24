####################################################################
#  corner_grocer_main.py                                           #
#  Name: Alysha Pursley                                            #
#  Date: August 3, 2025                                            #
#  Description:                                                    #
#    Main application for database-backed grocery frequency app    #
####################################################################

import sys
from db_handler import (
    connect_to_db,
    create_table,
    insert_or_update_item,
    get_all_frequencies,
    get_frequency_for_item,
    get_frequencies_sorted_by_count
)
import grocery_utils as utils

####################################################################
#  Input Validation: Menu Choice (1–9)                             #
####################################################################
def get_validated_choice():
    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 9:
            return choice
    except ValueError:
        pass
    print("Invalid input. Please enter a number from 1 to 9.")
    return 0

####################################################################
#  Input Validation: Item Name (letters & spaces only)             #
####################################################################
def is_valid_item_name(item_name):
    return all(ch.isalpha() or ch.isspace() for ch in item_name)

####################################################################
#  Print Main Menu                                                 #
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
#  Main Program                                                    #
####################################################################
if __name__ == "__main__":
    DB_FILE = "grocery.db"
    INPUT_FILE = "grocery_input.txt"

    ####################################################################
    # Connect to database                                              #
    ####################################################################
    conn = connect_to_db(DB_FILE)
    if not conn:
        sys.exit(1)

    ####################################################################
    # Ensure table exists                                              #
    ####################################################################
    create_table(conn)

    ####################################################################
    # Read input file and populate DB                                  #    
    ####################################################################
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                item = line.strip().lower()
                if item:
                    insert_or_update_item(conn, item)
        print(f"Processed input file: {INPUT_FILE}")
    except FileNotFoundError:
        print(f"Error: File '{INPUT_FILE}' not found.")
        sys.exit(1)

    ####################################################################
    # Interactive menu loop                                            #
    ####################################################################
    running = True
    while running:
        print_menu()
        choice = get_validated_choice()

        if choice == 1:
            query = input("Enter item name: ").strip()
            if not query:
                print("Please enter a non-empty item name.")
                continue
            if not is_valid_item_name(query):
                print("Invalid item name. Use letters and spaces only.")
                continue
            freq = get_frequency_for_item(conn, query.lower())
            print(f"{query} was purchased {freq} time(s).")

        elif choice == 2:
            print("\nAll item frequencies:")
            all_freq = get_all_frequencies(conn)
            for item, freq in all_freq.items():
                print(f"{item}: {freq}")

        elif choice == 3:
            print("\nItem frequency histogram:")
            all_freq = get_all_frequencies(conn)
            for item, freq in all_freq.items():
                print(f"{item}: {'*' * freq}")

        elif choice == 4:
            print("\nItems sorted alphabetically (A–Z):")
            freq_data = get_all_frequencies(conn)
            utils.sort_alpha(freq_data)

        elif choice == 5:
            print("\nItems sorted by frequency (high → low):")
            freq_data = get_frequencies_sorted_by_count(conn)
            utils.sort_by_freq(freq_data)

        elif choice == 6:
            query = input("Enter item to search: ").strip()
            if not query:
                print("Please enter a non-empty item name.")
                continue
            if not is_valid_item_name(query):
                print("Invalid item name. Use letters and spaces only.")
                continue
            freq_data = get_all_frequencies(conn)
            utils.search_item(freq_data, query)

        elif choice == 7:
            try:
                with open("frequency_list.dat", "w", encoding="utf-8") as f:
                    for item, freq in get_all_frequencies(conn).items():
                        f.write(f"{item} {freq}\n")
                print("Saved to frequency_list.dat")
            except Exception as e:
                print(f"Failed to save frequency list: {e}")

        elif choice == 8:
            try:
                with open("frequency_histogram.dat", "w", encoding="utf-8") as f:
                    for item, freq in get_frequencies_sorted_by_count(conn).items():
                        f.write(f"{item}: {'*' * freq}\n")
                print("Saved to frequency_histogram.dat")
            except Exception as e:
                print(f"Failed to save histogram: {e}")

        elif choice == 9:
            print("Goodbye!")
            running = False

    ####################################################################
    # Close database connection                                        #
    ####################################################################
    conn.close()
    print("Database connection closed.")
