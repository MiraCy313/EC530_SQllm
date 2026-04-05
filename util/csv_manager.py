###############
# CSV manager
# manage csv readin, data readin
###############
from pathlib import Path
import pandas as pd
import sqlite3

###############
def CSV_reader(csv_path):
    ### check if a path is valid. If yes, return a pandas csv_reader. If not, raise Error
    # csv_path: csv file path given by user
##############
    cpath = Path(csv_path)
    if not cpath.exists():
        raise ValueError("File does not exsist!")
    elif cpath.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are accepted!")
    else:
        cfile = pd.read_csv(cpath)
        return cfile


def CSV_import(csv_inst, table_name, cursor):
    ### import data into db table
    # csv_inst: pandas csv_reader instance
    # table_name: user defined new table name
    # cursor: sqlite db cursor object (a connection to current db)
###############
    # add table name check (avoid same name or accidentally overwriting)
###############
    columns_name = list(csv_inst.columns)
    placeholders = ",".join(["?"] * len(columns_name))
    data = csv_inst.itertuples(index=False, name=None)      
    ######## change here, try to match data to columns_name
    cursor.executemany(
        f"INSERT INTO {table_name} ({", ".join(columns_name)}) VALUES ({placeholders})",
        data
    )
    print("CSV import complete!")
    pass


###############
