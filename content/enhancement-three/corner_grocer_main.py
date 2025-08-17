#######################################################################
#  corner_grocer_main.py                                               #
#  Name: Alysha Pursley                                                #
#  Date: July 2025                                                     #
#  Description:                                                        #
#    Enhancement Three (Databases):                                    #
#      - Replaces in-memory dict with SQLite persistence               #
#      - Preserves all existing features from Enhancement Two          #
#      - Adds safe, parameterized DB operations and exports            #
#######################################################################

#######################################################################
#  Imports                                                             #
#  sys for exit control                                                #
#  db_handler provides DB operations (connect, query, export)          #
#  grocery_utils provides sorting & searching helpers                  #
#######################################################################
import sys
import db_handler as db
import grocery_utils as utils


#######################################################################
#  is_valid_item_name                                                  #
#  Validates item names to letters and spaces only.                    #
#######################################################################
def is_valid_item_name(item_name: str) -> bool:
    return all(ch.isalpha() or ch.isspace() for ch in item_name)


#######################################################################
#  get_validated_choice                                                #
#  Safely reads a menu choice between 1 and 9; returns 0 on error.    #
#######################################################################
def get_validated_choice() -> int:
    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 9:
            return choice
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 9.")
        return 0


#######################################################################
#  print_menu                                                          #
#  Displays all available actions for the program.                     #
#######################################################################
def print_menu() -> None:
    print("\n========== Corner Grocer Menu ==========")
    print("1. Look up item frequency")
    print("2. Print all items and frequencies (A–Z)")
    print("3. Print frequency histogram (A–Z)")
    print("4. Sort items alphabetically (A–Z)")
    print("5. Sort items by frequency (high → low)")
    print("6. Search for a specific item")
    print("7. Save frequency list to frequency_list.dat")
    print("8. Save histogram to frequency_histogram.dat")
    print("9. Exit program")
    sys.stdout.flush()


#######################################################################
#  main                                                                #
#  Program entry point for Enhancement Three.                          #
#######################################################################
def main() -> None:
    INPUT_FILE = "grocery_input.txt"   # same input content as earlier phases
    DB_FILE    = "grocery.db"          # created on first run if missing

    # Initialize database and load input file once at startup
    db.connect_to_db(DB_FILE)
    try:
        db.process_input_file(INPUT_FILE)
    except FileNotFoundError:
        # Already messaged by db layer; exit gracefully since DB is empty
        db.close_db()
        sys.exit(1)

    running = True
    while running:
        print_menu()
        choice = get_validated_choice()

        if choice == 0:
            # invalid input case already messaged; re-loop
            continue

        if choice == 1:
            item = input("Enter item name: ").strip()
            if not item:
                print("Please enter a non-empty item name.")
                continue
            if not is_valid_item_name(item):
                print("Invalid item name. Use letters and spaces only.")
                continue
            freq = db.get_item_frequency(item)
            print(f"{item} was purchased {freq} time(s).")

        elif choice == 2:
            print("\nAll item frequencies (A–Z):")
            db.print_all_items()

        elif choice == 3:
            print("\nItem frequency histogram (A–Z):")
            db.print_histogram()

        elif choice == 4:
            print("\nItems sorted alphabetically (A–Z):")
            # utils accepts dict or list of pairs; DB returns pairs
            pairs = db.get_all_items()
            utils.sort_alpha(pairs)

        elif choice == 5:
            print("\nItems sorted by frequency (high → low):")
            pairs = db.get_all_items()
            utils.sort_by_freq(pairs)

        elif choice == 6:
            query = input("Enter item to search: ").strip()
            if not query:
                print("Please enter a non-empty item name.")
                continue
            if not is_valid_item_name(query):
                print("Invalid item name. Use letters and spaces only.")
                continue
            pairs = db.get_all_items()
            utils.search_item(pairs, query)

        elif choice == 7:
            try:
                db.export_frequency_list("frequency_list.dat")
                print("Saved to frequency_list.dat")
            except Exception as e:
                print(f"Failed to save frequency list: {e}")

        elif choice == 8:
            try:
                db.export_histogram("frequency_histogram.dat")
                print("Saved to frequency_histogram.dat")
            except Exception as e:
                print(f"Failed to save histogram: {e}")

        elif choice == 9:
            print("Goodbye!")
            running = False

    db.close_db()


#######################################################################
#  Entry Point                                                         #
#######################################################################
if __name__ == "__main__":
    main()
