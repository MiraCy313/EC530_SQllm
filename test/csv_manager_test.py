###############
# testbench for csv_manager
###############
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(str(root_dir))

import util.csv_manager as csvm
import sqlite3

db_path = "./test.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    csv_path = input("Enter CSV path:")
    csv_file = csvm.CSV_reader(csv_path)
    csvm.CSV_import(csv_file, "test", cursor)
    conn.commit()
    conn.close
    pass
except ValueError as e:
    print(e)