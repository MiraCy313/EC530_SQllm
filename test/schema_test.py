###############
# testbench for csv_manager
###############
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(str(root_dir))

import util.schema_manager as schm
import util.csv_manager as csvm
import sqlite3

db_path = "test/test.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    csv_path = input("Enter CSV path:")
    csv_file = csvm.CSV_reader(csv_path)
    tb_name = schm.Schema_import(csv_file, cursor)
    csvm.CSV_import(csv_file, tb_name, cursor)
    conn.commit()
    conn.close
except ValueError as e:
    print(e)