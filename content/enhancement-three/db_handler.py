#
####################################################################
#  db_handler.py                                                                                                                                                    #
#  Name: Alysha Pursley                                                                                                                                       #
#  Date: July 2025                                                                                                                                                  #
#  Description:                                                                                                                                                        #
#    SQLite database layer for Corner Grocer enhancement three.                                                      #
#    Handles connection, table creation, item upserts, queries, ordered printing, and data          #
#   export.                                                                                                                                                                 #                                           
####################################################################

####################################################################
#  Imports                                                                                                                                                                  #
#  sqlite3 provides local relational storage and SQL execution                                                              #
#  typing is used only for helpful type hints (optional)                                                                             #
####################################################################
import sqlite3
from typing import List, Tuple, Optional

####################################################################
#  Module-level connection objects                                                                                                                 #
#  These are initialized by connect_to_db() and closed by close_db()                                               #
####################################################################
_conn: Optional[sqlite3.Connection] = None
_cur: Optional[sqlite3.Cursor] = None

####################################################################
#  connect_to_db                                                                                                                                                   #
#  Opens/creates SQLite DB and ensures the frequencies table exists.                                           #
####################################################################
def connect_to_db(db_name: str = "grocery.db") -> None:
    global _conn, _cur
    _conn = sqlite3.connect(db_name)
    _conn.execute("PRAGMA foreign_keys = ON;")
    _cur = _conn.cursor()
    _cur.execute(
        """
        CREATE TABLE IF NOT EXISTS frequencies (
            item  TEXT PRIMARY KEY,
            count INTEGER NOT NULL
        )
        """
    )
    _conn.commit()

####################################################################
#  close_db                                                                                                                                                               #
#  Cleanly closes cursor and connection to avoid file locks.                                                                    #
####################################################################
def close_db() -> None:
    global _conn, _cur
    try:
        if _cur is not None:
            _cur.close()
    finally:
        _cur = None
    try:
        if _conn is not None:
            _conn.close()
    finally:
        _conn = None

####################################################################
#  _ensure_ready                                                                                                                                                    #
#  Internal guard to verify DB is connected before use.                                                                           #
####################################################################
def _ensure_ready() -> None:
    if _conn is None or _cur is None:
        raise RuntimeError("Database not connected. Call connect_to_db() first.")

####################################################################
#  process_input_file                                                                                                                                             #
#  Reads each non-empty line, normalizes to lowercase, and updates                                                 #
#  the frequencies table. Uses an UPDATE-then-INSERT flow to 'upsert'.                                       #
####################################################################
def process_input_file(filename: str) -> None:
    _ensure_ready()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for raw in f:
                item = raw.strip().lower()
                if not item:
                    continue
                # UPDATE first; if no row updated, INSERT new
                _cur.execute("UPDATE frequencies SET count = count + 1 WHERE item = ?", (item,))
                if _cur.rowcount == 0:
                    _cur.execute("INSERT INTO frequencies(item, count) VALUES (?, ?)", (item, 1))
        _conn.commit()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        raise

####################################################################
#  get_item_frequency                                                                                                                                          #
#  Returns the current count for an item, or 0 if it does not exist.                                                         #
####################################################################
def get_item_frequency(item: str) -> int:
    _ensure_ready()
    _cur.execute("SELECT count FROM frequencies WHERE item = ?", (item.lower(),))
    row = _cur.fetchone()
    return int(row[0]) if row else 0

####################################################################
#  get_all_items                                                                                                                                                        #
#  Returns list[(item, count)] of all rows in the table.                                                                                 #
####################################################################
def get_all_items() -> List[Tuple[str, int]]:
    _ensure_ready()
    _cur.execute("SELECT item, count FROM frequencies")
    rows = _cur.fetchall()
    # Normalize to (str, int)
    return [(str(r[0]), int(r[1])) for r in rows]

####################################################################
#  print_all_items                                                                                                                                                     #
#  Displays all items alphabetically with counts.                                                                                           #
####################################################################
def print_all_items() -> None:
    _ensure_ready()
    _cur.execute("SELECT item, count FROM frequencies ORDER BY item ASC")
    for item, count in _cur.fetchall():
        print(f"{item}: {count}")
        
####################################################################
#  print_histogram                                                                                                                                                  #
#  Displays alphabetical list where each line shows item and stars equal to its frequency.            #
####################################################################
def print_histogram() -> None:
    _ensure_ready()
    _cur.execute("SELECT item, count FROM frequencies ORDER BY item ASC")
    for item, count in _cur.fetchall():
        print(f"{item}: {'*' * int(count)}")

####################################################################
#  export_frequency_list                                                                                                                                      #
#  Writes "item count" lines sorted alphabetically to a file.                                                                        #
####################################################################
def export_frequency_list(filename: str = "frequency_list.dat") -> None:
    _ensure_ready()
    with open(filename, "w", encoding="utf-8") as out:
        _cur.execute("SELECT item, count FROM frequencies ORDER BY item ASC")
        for item, count in _cur.fetchall():
            out.write(f"{item} {int(count)}\n")

####################################################################
#  export_histogram                                                                                                                                              #
#  Writes "item: *****" lines sorted by count desc, then item asc.                                                             #
####################################################################
def export_histogram(filename: str = "frequency_histogram.dat") -> None:
    _ensure_ready()
    with open(filename, "w", encoding="utf-8") as out:
        _cur.execute(
            """
            SELECT item, count
              FROM frequencies
             ORDER BY count DESC, item ASC
            """
        )
        for item, count in _cur.fetchall():
            out.write(f"{item}: {'*' * int(count)}\n")
